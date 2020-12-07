from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint("users", __name__) #"users" is the name of our blueprint 



@users.route('/register', methods=['GET', 'POST']) #(Ctrl+Shift+L) for multi-line selction
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created! You can now Log In', 'success')
        return redirect(url_for('users.login'))
    return render_template("register.html", title='Register', form=form) #form=form --> so we caan control from our form.py code by passing an instance


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #if user exsists and the stored hashed pass == hashed givien loin pass
            login_user(user, remember=form.remember.data) #then login the user
            next_page = request.args.get('next') #args is a dict but dont use [] this way will through error
            return redirect(next_page) if next_page else redirect(url_for("main.home")) #! this is new for me in python tirnary conditional this way we can redirect the uer to accunt page hen he ask for it after login and if he didbnt' ask(typied it in the url/account) then he goes to the home page
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title='Login', form=form) 

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))




#TODO 'POST'
#we use it so our browser don't ask the user are you sure you wnt to leafve the page
@users.route("/account", methods=['GET', 'POST']) 
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) #get img from static folder where curent suer image data
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)




@users.route("/user/<string:username>")
def user_posts(username): #! this so when you click username you will be taken to a page full of there posts
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404() #get first user(search by id) or 404
    posts = (Post.query.filter_by(author=user)
                  .order_by(Post.date_posted.desc())
                  .paginate(page=page, per_page=5)
         )
    return render_template('user_posts.html', posts=posts, user=user)

    

@users.route("/reset_password", methods=['GET', 'POST']) #TODO a route so they can put there email so we send it and the rout under it will be to reset the password
def reset_request():
    if current_user.is_authenticated:#make sure they are loged out before we reset there password
        return redirect(url_for('main.home'))
    
    Form = RequestResetForm()#using the RequestResetform along wiht the reset_request.html we render it here through this rout it all comes together like Magic WOW!!
    if Form.validate_on_submit(): #if the form where created then we need to validate it
        user = User.query.filter_by(email=Form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your password", "info")
        return redirect(url_for('users.login'))
        
    return render_template('reset_request.html', title='Reset Password', form=Form)
    
    
@users.route("/reset_password/<token>", methods=['GET', 'POST']) #TODO a route to get there new password and since we would like to make sure it is the user not a melicios attacker we use token JWS
def reset_token(token):
    if current_user.is_authenticated:#make sure they are loged out before we reset there password
        return redirect(url_for('main.home'))
    
    user = User.verify_reset_token(token) #to verify that this is the user token not an attacker using the medthod created in the model.py
                                          # this will retun the user_id or (none if expired or this is not a user)
    if user is None:
        flash('That is an invalid token', 'warning') #we can pass a class and it is the bootstrap warning so it is yellow/red
        return redirect(url_for('users.reset_request'))
    
    Form = ResetPasswordForm()
    if Form.validate_on_submit():#just like registeration route
        hashed_pw = bcrypt.generate_password_hash(Form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash('Your Password has been updated! You can now Log In', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('reset_token.html', title='Reset Password', form=Form)
    
    

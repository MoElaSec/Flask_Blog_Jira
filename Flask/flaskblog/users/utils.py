import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail



def save_picture(form_picture):
    random_hex = secrets.token_hex(8) #don't store the name of the imported file since it's may collide with an exsitance file from ours so it is better to randomize the name
    _, f_ext = os.path.splitext(form_picture.filename) #grap the file extention (returns filename + falename with the extention we don't need the first we just need it with the extention to validate it inside our form UpdateAccount()  when we store it inside picture ver)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125) #always rezise the image we git so it becomes as we want to be (also take less space + faster load)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


#TODO Using Flask-Mail (pip install flask-mail)
def send_reset_email(user): #used to send an email with the info that you requested to change your password
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                  sender='noreplay@demo.com',
                   recipients=[user.email]) #make sure not to spoof the email so it doesn't end in the spam use your email
    msg.body = f"""To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
        
if you didn't make this request then simply ignore this email, and no changes will be made.
"""# _external  you can use jinja2 templte but not here so true not long enough
    
    mail.send(msg)
   
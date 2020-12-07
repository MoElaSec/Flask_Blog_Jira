from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint("main", __name__)


#! Paginatin: process of turing punch of data to pages..
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int) #let's get a page where defualt is 1 with int so no one can pass anything other then int as a page num.
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3) #make only 5 posts avilable per page..
    return render_template('home.html', posts=posts)


@main.route('/about')
def about(): 
    return render_template("about.html", title='About')


 
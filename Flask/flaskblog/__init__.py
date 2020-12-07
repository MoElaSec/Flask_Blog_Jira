from flask import Flask
from flask_jira import FlaskJIRA
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


my_jira_client = FlaskJIRA()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #login is name of function (if you tried to go to account without having one then you get redirected to the login page)
login_manager.login_message_category = 'info' #improve ask login looks(UI)
mail = Mail() #initialize mail like everything else



#don't create the routs before you initialize the app
#! we are importing this one here to handle a specific error discussed in Package Structure Video
#? from flaskblog import route 
# it has been commented afte the blueprint video since now we re structred our app


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    my_jira_client.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

#! Notice how we are importing the routes down here
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users) #registering our Blueprint
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

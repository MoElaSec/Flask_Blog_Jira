import os


# >>> import secrets  #!'this is how I crteated the Secret
# >>> secrets.token_hex(16)

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') didn't setup env ver in windows path
    SECRET_KEY = '03bff4ba217348941df2104aafde0195'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #!(///) these means that the sqlite(basicaly a file) will be created here..

#? to send email when they request reseting password (using gmail [google mail server] )
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "mark.hacker.1996@gmail.com" #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = "Hate.Hamod-123" #os.environ.get('EMAIL_PASS')

#? For the Jira Config
    JIRA_SERVER =  "https://al-addin.atlassian.net/"
    # JIRA_OPTIONS =  "https://al-addin.atlassian.net/"
    JIRA_BASIC_AUTH = ('mohd.debrecen@gmail.com', 'lou8WpfND4Oa7pVKFWFW56EC')
    # JIRA_OAUTH = 
    # JIRA_JWT =

#! HOw thing used to be before blueprints
    # app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = "mark.hacker.1996@gmail.com" #this is to make it hidden os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = "Hate.Hamod-123" #os.environ.get('EMAIL_PASS')
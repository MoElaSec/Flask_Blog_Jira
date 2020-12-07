import os


# >>> import secrets  #!'this is how I crteated the Secret
# >>> secrets.token_hex(16)

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') didn't setup env ver in windows path
    SECRET_KEY = 'your_secret_key'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #!(///) these means that the sqlite(basicaly a file) will be created here..

#? to send email when they request reseting password (using gmail [google mail server] )
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your_email" #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = "your_pass3" #os.environ.get('EMAIL_PASS')

#? For the Jira Config
    JIRA_SERVER =  "https://your_attlassian.atlassian.net/"
    # JIRA_OPTIONS =  
    JIRA_BASIC_AUTH = ('your_mail@gmail.com', 'tokin')
    # JIRA_OAUTH = 
    # JIRA_JWT =


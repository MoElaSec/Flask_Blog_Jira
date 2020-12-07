from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

#TODO there're also errorhandler instead of the app_ but that's only works in this temblet but we want soomething to work every where  

#Page doesn't exist
@errors.app_errorhandler(404) #! Notice how it's not route since this is a error handler first time doing this
def error_404(error): #! treat it like a rout
    return render_template("errors/404.html"), 404 #? in flask you actually return two values the second being the status code[by default: 200] thus why we never wrote before 


@errors.app_errorhandler(403) #Forbidden
def error_403(error):
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500) #General server error
def error_500(error):
    return render_template("errors/500.html"), 500
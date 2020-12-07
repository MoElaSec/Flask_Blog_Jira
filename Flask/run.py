# Following YT Tut:https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
#by: Corey Schafer  
from flaskblog import create_app

app = create_app()


#!#############################################
if __name__ == '__main__':
    app.run(debug=True)
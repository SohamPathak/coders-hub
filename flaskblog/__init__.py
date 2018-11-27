# CHECK THE LINK FOR BOOTSTRAP CLASSES https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#the below states where our login routes are located here the login is the function name of the route
login_manager.login_view = 'login'
#the below display the meassge that the login is reguired in bootstrap class -info
login_manager.login_message_category = 'info'

from flaskblog import routes
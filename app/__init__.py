from flask import Flask
from config import Config 
# We moved the instance of flask from the run.py file to the app file 
# Also need to say from app import app in run.py file now to link it

app = Flask(__name__)
#The __name__ variable passed to the Flask class is a Python predefined variable, 
# which is set to the name of the module in which it is used
# Hover over flask - tells us that template folder is "templates"

# secret key (do not hard code this in but okay for now)
app.config.from_object(Config)

# from app import forms

from app import routes
# routes must go at the bottom (specific to flask)
# from app import routes links routes to the app





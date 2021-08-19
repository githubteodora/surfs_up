# we can import the dependency we need. This dependency will enable your code to access all that Flask has to offer.
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite") # The create_engine() function allows us to access and query our SQLite database file. 
Base = automap_base() # let's reflect the database into our classes; this is like a translation - everything in the dataset becomes a class
Base.prepare(engine, reflect=True) # Flask function we use to reflect the tables

# With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier in this module. 
# We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Finally, create a session link from Python to our database with the following code
session = Session(engine)

# Next, we need to define our app for our Flask application.
# Set Up Flask
# Create a New Flask App Instance
app = Flask(__name__)

# You probably noticed the __name__ variable inside of the Flask() function. Let's pause for a second and identify what's going on here.
# This __name__ variable denotes the name of the current function. You can use the __name__ variable to determine if your code is being run 
# from the command line or if it has been imported into another piece of code. Variables with underscores before and after them are called magic methods in Python.

# Create Flask Routes
# First, we need to define the starting point, also known as the root. To do this, we'll use the function @app.route('/').
@app.route('/')
# Notice the forward slash inside of the app.route? This denotes that we want to put our data at the root of our routes. The forward slash is commonly known as the highest level of hierarchy in any computer system.

# Next, create a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route below @app.route()
# Create the Welcome Route( the homepage.)
# All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. We'll use f-strings to display them for our investors:
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# Run a Flask App
# The process of running a Flask app is a bit different from how we've run Python files. 
# To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code. 
# then, type flask run in anaconda powershell; then paste the URL into a browser.
# Question - why is it showing on one line?
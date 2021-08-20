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
# adding connect_args to avoid an error, see https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread': False}) # The create_engine() function allows us to access and query our SQLite database file. 
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
    <h1>Welcome to the Climate Analysis API!</h1></br>
    Available Routes:</br>
    /api/v1.0/precipitation</br>
    /api/v1.0/stations</br>
    /api/v1.0/tobs</br>
    /api/v1.0/temp/start/end
    ''')
# the text of the routes can be absolutely anything we decide!

# Run a Flask App
# The process of running a Flask app is a bit different from how we've run Python files. 
# To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code. 
# then, type flask run in anaconda powershell; then paste the URL into a browser.
# Question - why is it showing on one line? -> we can use html tags to fix this! 


# Precipitation Route
# The next route we'll build is for the precipitation analysis. This route will occur separately from the welcome route.
# Every time you create a new route, your code should be aligned to the left in order to avoid errors.
# Notice the .\ in the first line of our query? This is used to signify that we want our query to continue on the next line. 
# You can use the combination of .\ to shorten the length of your query line so that it extends to the next line.

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365) # First, we want to add the line of code that calculates the date one year ago from the most recent date in the database
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= prev_year).all()
    # Finally, we'll create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)



# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) # We want to start by unraveling our results into a one-dimensional array. To do this, we want to use thefunction np.ravel(), with results as our parameter
    return jsonify(stations=stations) # You may notice here that to return our list as JSON, we need to add stations=stations. This formats our list into JSON.


@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Statistics Route
# Our last route will be to report on the minimum, average, and maximum temperatures. However, this route is different from the previous ones in that we will have to provide both a starting and ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# We need to add parameters to our stats()function: a start parameter and an end parameter.
def stats(start=None, end=None): 
# With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
# Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. We'll need to query our database using the list that we just made. 
# Then, we'll unravel the results into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.
# In the following code, take note of the asterisk in the query next to the sel list. Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    # Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. 
    # We'll use the sel list, which is simply the data points we need to collect. Let's create our next query, which will get our statistics data.
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)    
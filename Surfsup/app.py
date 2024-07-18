# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session from Python to the DB
    session = Session(engine)

    """Return a list of Precipitation Data including Date and Amount of Precipitation"""
    # Query to retrieve the last 12 months of precipitation data
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= start_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precip_data
    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session from Python to the DB
    session = Session(engine)

    """Return a list of stations from the dataset"""
    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session from Python to the DB
    session = Session(engine)

    """Return a list of Temp Obvs Data including Date and Amount of Temp Obvs"""
    # Query to retrieve the last 12 months of temp obvs data
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= start_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of tobs_data
    tobs_data = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

@app.route("/api/v1.0/<start_date>")
def start(start_date):
    # Create our session from Python to the DB
    session = Session(engine)

    """Return a JSON list of the min temp, avg temp, max temp for >= given start date"""
    # Query to calculate tmin, tavg, and tmax for all dates greater than and equal to the start date.
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    session.close()

    # Create a dictionary from the tmin, tavg, tmax data
    temp_data = []
    for tmin, tavg, tmax in results:
        temp_dict = {}
        temp_dict["tmin"] = tmin
        temp_dict["tavg"] = tavg
        temp_dict["tmax"] = tmax
        temp_data.append(temp_dict)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date, end_date):
    # Create our session from Python to the DB
    session = Session(engine)

    """Return a JSON list of the min temp, avg temp, max temp for given start-end range"""
    # Query to calculate tmin, tavg, and tmax for for dates between the start and end date inclusive.
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    # Create a dictionary from the tmin, tavg, tmax data
    temp_data = []
    for tmin, tavg, tmax in results:
        temp_dict = {}
        temp_dict["tmin"] = tmin
        temp_dict["tavg"] = tavg
        temp_dict["tmax"] = tmax
        temp_data.append(temp_dict)

    return jsonify(temp_data)

if __name__ == '__main__':
    app.run(debug=True)
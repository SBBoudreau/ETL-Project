# Docs on session basics
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html

import os

import numpy as np
import pandas as pd
import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Database Setup
#################################################
pg_user = 'postgres'
pg_password = '1988'
db_name = 'properties_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
realtor = Base.classes.realtor
zillow = Base.classes.zillow

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
        f"/api/v1.0/listofzipcodes"
    )


@app.route("/api/v1.0/listofzipcodes")
def names():
    """Return a list of Property Statistics for all available Zipcodes in Texas  """

    # Query all props
    session = Session(engine)

    property_join = pd.read_sql(session.query(realtor.zipcode,zillow.statename, 
                        zillow.countyname, zillow.cityname,
                        realtor.total_listing_count,
                        realtor.median_listing_price,
                        realtor.average_listing_price,
                        realtor.median_listing_price_per_square_foot, 
                        zillow.forecasteddate,
                        zillow.forecastyoypctchange)\
                        .filter(realtor.zipcode == zillow.zipcode).limit(50).statement, engine).sort_values(by='average_listing_price')
                                                                    
    

    # close the session to end the communication with the database
    session.close()

    # Create a dictionary from the row data and append to a list of all_props
    all_props = property_join.to_dict(orient='records')

    return jsonify(all_props)

if __name__ == '__main__':
    app.run(debug=True)

# Sqlalchemy_Challenge
 Use SQLAlchemy to connect to a database, reflect the schema, and perform queries.
 Reflect an existing database into a new model and reflect the table
 View all of the classes that automap found and  save references to each table
 Create our session (link) from Python to the DB

Exploratory precipitation analysis
 Find the most recent data in the dataset
 A query to retrieve the last 12 months of precipitation data and plot the results. 
Starting from the most recent data point in the database.
 Calculated the date one year from the last date in data set
 A query to retrieve the data and precipitation scores
Save the query results as a Pandas DataFrame. Explicitly set the column names
Use Pandas Plotting with Matplotlib to plot the data
 Use Pandas to calculate the summary statistics for the precipitation data

 Station analysis
 A query to calculate the total number of stations in the dataset
 A query to find the most active stations (i.e. which stations have the most rows?)
 Also List the stations and their counts in descending order.
 
 We can see which stations are the most and the least active.
 Station - USC00519281 have the most rows
  Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.

 We will calculate the minimum, maximum, and average temperatures with the following functions: 
 func.min, func.max, and func.avg. 
 Also we'll be filtering out everything but the most active station - USC00519281. 
 Finally, add the .all() function to return our results as a list.The results show that the low (minimum) temperature is 54 degrees,the high (maximum) temperature is 85 degrees, and the average temperature is approximately 72 degrees 
 Query to find station with highest number of temp obvs and also query the last 12 months of temp obvs for that station, using the start and end dates found
 Saved the results in DataFrame and Plot as a Histogram

 Also for the app.py folder, design a flask API based on the queries that was developed.

 Import the dependencies, database setup, reflect an existing database into a new mode.
 Reflect the tables, save references to each table.
 Create our session link from python to the DB, flask setup, flask routes.
 Also query to retrieve the last 12 months, created a dictionary from the row data and append to a list of precip_data.
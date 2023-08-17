
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask,render_template, jsonify
from flask_cors import cross_origin

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder='templates', static_folder='static')

#################################################
# Database Setup 
#i named the server project 3 and the database "ticketmaster"
#################################################

def create_connection():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='Project_4',
        user='postgres',
        password='postgres'
    )
    return conn




@app.route('/')
def home():
    # Run function to connect to the database
    conn = create_connection()
    cur = conn.cursor()

    # Select all of the columns from the table
    cur.execute('SELECT * FROM table')
    rows = cur.fetchall()

    cur.close()
    conn.close()

    # Convert the rows to a list of dictionaries
    data = []
    for row in rows:
        data.append({
            'event_id': row[0],
            'event_name': row[1],
            'venue_id': row[2],
            'event_url': row[3],
            'image_url': row[4],
            'startDate': row[5],
            'genre_id': row[7],
            'min_price': row[9],
            'max_price': row[10]
            # Add more columns as needed
        })
    return jsonify(data)








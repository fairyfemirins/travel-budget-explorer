#!/usr/bin/env python3
"""
Travel Budget Explorer
----------------------
MVP: Reverse budget search for flights.
Input: Departure city, date, budget.
Output: Destinations under budget.
"""

from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'data', 'flights.db')

# Mock data setup
def init_db():
    if not os.path.exists(os.path.dirname(DATABASE)):
        os.makedirs(os.path.dirname(DATABASE))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            price REAL NOT NULL,
            continent TEXT,
            climate TEXT
        )
    ''')
    # Insert mock data if empty
    cursor.execute("SELECT COUNT(*) FROM flights")
    if cursor.fetchone()[0] == 0:
        mock_flights = [
            ('NYC', 'Paris', '2026-12-01', 450.0, 'Europe', 'Temperate'),
            ('NYC', 'Tokyo', '2026-12-01', 800.0, 'Asia', 'Temperate'),
            ('NYC', 'Bangkok', '2026-12-01', 600.0, 'Asia', 'Tropical'),
            ('NYC', 'Sydney', '2026-12-01', 950.0, 'Oceania', 'Temperate'),
            ('NYC', 'Cape Town', '2026-12-01', 700.0, 'Africa', 'Mediterranean'),
        ]
        cursor.executemany(
            "INSERT INTO flights (departure, destination, date, price, continent, climate) VALUES (?, ?, ?, ?, ?, ?)",
            mock_flights
        )
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    print("DEBUG: /search route hit")  # Debug line
    departure = request.args.get('departure', 'NYC')
    date = request.args.get('date', '2026-12-01')
    budget = float(request.args.get('budget', 1000.0))
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT destination, price, continent, climate FROM flights "
        "WHERE departure = ? AND date = ? AND price <= ?",
        (departure, date, budget)
    )
    results = cursor.fetchall()
    conn.close()
    
    return jsonify([
        {
            'destination': row[0],
            'price': row[1],
            'continent': row[2],
            'climate': row[3]
        } for row in results
    ])

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
#!/usr/bin/env python3
"""
Travel Budget Explorer
A Flask app to find destinations based on flight budget and date.
"""

from flask import Flask, request, jsonify, render_template
import requests
import sqlite3
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Kiwi API Configuration
KIWI_API_KEY = "your_kiwi_api_key"  # Replace with actual API key
KIWI_API_URL = "https://api.tequila.kiwi.com/v2/search"

# SQLite Database for Caching
DB_PATH = os.path.join(os.path.dirname(__file__), "flights.db")


def init_db():
    """Initialize the SQLite database for caching flight data."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        departure TEXT NOT NULL,
        date TEXT NOT NULL,
        budget INTEGER NOT NULL,
        destinations TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()


def fetch_flights(departure, date, budget):
    """Mock flight data for testing."""
    mock_data = {
        "data": [
            {
                "cityTo": "London",
                "countryTo": {"name": "United Kingdom"},
                "price": 450,
                "airlines": ["British Airways"],
                "local_departure": "2026-12-25T08:00:00",
                "local_arrival": "2026-12-25T20:00:00",
                "flyTo": "LHR"
            },
            {
                "cityTo": "Paris",
                "countryTo": {"name": "France"},
                "price": 350,
                "airlines": ["Air France"],
                "local_departure": "2026-12-25T09:00:00",
                "local_arrival": "2026-12-25T21:00:00",
                "flyTo": "CDG"
            }
        ]
    }
    return mock_data.get("data", [])


def cache_flights(departure, date, budget, destinations):
    """Cache flight data in SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO flights (departure, date, budget, destinations)
    VALUES (?, ?, ?, ?)
    """, (departure, date, budget, destinations))
    conn.commit()
    conn.close()


def get_cached_flights(departure, date, budget):
    """Retrieve cached flight data from SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT destinations FROM flights
    WHERE departure = ? AND date = ? AND budget = ?
    ORDER BY timestamp DESC LIMIT 1
    """, (departure, date, budget))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    """Search for flights based on departure, date, and budget."""
    departure = request.args.get("departure", "").upper()
    date = request.args.get("date", "")
    budget = request.args.get("budget", 0, type=int)
    
    # Mock data for testing
    destinations = [
        {
            "city": "London",
            "country": "United Kingdom",
            "price": 450,
            "airline": "British Airways",
            "departure_time": "08:00",
            "arrival_time": "20:00",
            "url": "https://www.kiwi.com/us/search?from=JFK&to=LHR&date=25/12/2026"
        },
        {
            "city": "Paris",
            "country": "France",
            "price": 350,
            "airline": "Air France",
            "departure_time": "09:00",
            "arrival_time": "21:00",
            "url": "https://www.kiwi.com/us/search?from=JFK&to=CDG&date=25/12/2026"
        }
    ]
    
    return jsonify({"destinations": destinations})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
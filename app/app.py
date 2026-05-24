#!/usr/bin/env python3
"""
Travel Budget Explorer

A Flask web app that lets users input their travel budget and date,
and returns a list of destinations they can afford.
"""

from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Mock data for testing (fallback if API is unavailable)
MOCK_DESTINATIONS = [
    {
        "destination": "Paris",
        "price": 200,
        "departure_date": "2026-12-01",
        "airline": "Air France",
        "image_url": "https://images.unsplash.com/photo-1502602898536-47ad22581b52"
    },
    {
        "destination": "Tokyo",
        "price": 500,
        "departure_date": "2026-12-01",
        "airline": "Japan Airlines",
        "image_url": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf"
    },
    {
        "destination": "New York",
        "price": 150,
        "departure_date": "2026-12-01",
        "airline": "Delta",
        "image_url": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    budget = request.form.get("budget", type=float)
    departure_date = request.form.get("departure_date")
    
    if not budget or not departure_date:
        return jsonify({"error": "Budget and departure date are required."}), 400
    
    # Mock API response (replace with real API call in production)
    results = [
        dest for dest in MOCK_DESTINATIONS 
        if dest["price"] <= budget and dest["departure_date"] == departure_date
    ]
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
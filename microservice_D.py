"""Saves watchlist, fetches watchlist for persistent data storage"""

from flask import Flask, jsonify, request, json
import os

app = Flask(__name__)

watchlist_file = "watchlist.json"

@app.route('/save_watchlist', methods=['POST'])
def save_watchlist():
    """Saves the watchlist that is passed in"""
    try:
        # Get watchlist data (list of stocks) else returns default empty list
        watchlist_data = request.json.get('watchlist', [])
        # Add to file
        with open(watchlist_file, 'w') as file:
            json.dump(watchlist_data, file)
        return jsonify({"message":"Watchlist saved successfully"}), 200
    except Exception as e:
        return jsonify({"message":"Save unsuccessful"}), 500

@app.route('/load_watchlist', methods=['GET'])
def load_watchlist():
    """Passes the watchlist as a response"""
    # If file exist, return contents as json payload
    if os.path.exists(watchlist_file):
        with open(watchlist_file, 'r') as file:
            watchlist_data = json.load(file)
            return jsonify(watchlist_data), 200
    else:
        return []

if __name__== '__main__':
    app.run(debug = True, port=5003)
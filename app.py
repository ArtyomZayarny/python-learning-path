#!/usr/bin/env python3
"""
Entry point for the Number Guessing Game Flask application.
This file allows Render to easily find and run the Flask app.
"""

import sys
import os

# Add the guess_number_game directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'guess_number_game'))

# Import the Flask app from the guess_number_game module
from guess_number_game.app import app

# This is needed for Gunicorn to find the app
application = app

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

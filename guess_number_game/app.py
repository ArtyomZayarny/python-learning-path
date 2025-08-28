#!/usr/bin/env python3
"""
Entry point for the Number Guessing Game Flask application.
This file allows Render to easily find and run the Flask app.
"""

import sys
import os

# Import the Flask app from the flask_app module
from flask_app import app

# This is needed for Gunicorn to find the app
application = app

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

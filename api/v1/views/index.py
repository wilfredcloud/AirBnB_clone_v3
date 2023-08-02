#!/usr/bin/python3
"""View index"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns status
    """
    return jsonify({"status": "Ok"})

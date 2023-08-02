#!/usr/bin/python3
"""index for the api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns status"""
    return jsonify({"status": "Ok"})

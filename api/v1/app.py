#!/usr/bin/python3
"""
The application entry point
"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(obj):
    """Calls close method"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Page not found error"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """Main"""
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host, int(port), threaded=True)

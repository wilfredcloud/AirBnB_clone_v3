#!/usr/bin/python3
"""index for the api"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns status"""
    return jsonify({"status": "Ok"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def object_stats():
    """Returns stats of each object"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]
    stat_objs = {}
    for i in range(len(names)):
        stat_objs[names[i]] = storage.count(classes[i])

    return jsonify(stat_objs)

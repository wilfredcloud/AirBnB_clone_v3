#!/usr/bin/python3
"""View for state objects"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import abort, make_response, request, jsonify


@app_views.route('/states',  methods=['GET'], strict_slashes=False)
def get_all_states():
    """Get all states"""
    states = storage.all(State).values()
    list_states = [state.to_dict() for state in states]
    return jsonify(list_states)


@app_views.route('/states/<state_id>',  methods=['GET'], strict_slashes=False)
def get_states_by_id(state_id):
    """Get states by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delete state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create states"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update states"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)

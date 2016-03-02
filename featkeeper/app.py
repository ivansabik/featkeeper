# api.py
from flask import Flask, jsonify, Response
from models import FeatureRequest
import shortuuid
from pymongo import MongoClient
from bson import json_util, ObjectId
import json

API_ROOT_URL = '/api/v1'

app = Flask(__name__)

# Client app serve static files for HTML index and app.js
@app.route('/')
def client_app_html():
    return app.send_static_file('index.html')

@app.route('/app.js')
def client_app_js():
    return app.send_static_file('app.js')

@app.route('/app.css')
def client_app_css():
    return app.send_static_file('app.css')

# API endpoints
@app.route(API_ROOT_URL + '/feature-request', methods=['GET'])
def feature_requests_all_read():
    feature_request = FeatureRequest()
    feature_requests = feature_request.find_all()
    return jsonify(feature_requests=feature_requests)

@app.route(API_ROOT_URL + '/feature-request/<feature_request_id>', methods=['GET'])
def feature_request_by_id_read(feature_request_id):
    feature_request = FeatureRequest()
    feature_request = feature_request.find_by_id(feature_request_id)
    return jsonify(feature_request)

@app.route(API_ROOT_URL + '/feature-request', methods=['PUT'])
def feature_request_add():
    return jsonify({})

@app.route(API_ROOT_URL + '/feature-request', methods=['POST'])
def feature_requests_update():
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint does not exist'
    }), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
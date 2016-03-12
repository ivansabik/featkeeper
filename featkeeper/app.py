'''
api.py
Implements REST API endpoints for feature requests, for dev also serving static files
In production static files handled by server
Eventually will also implement /agent and /client
'''

from flask import Flask, jsonify, Response, request
from models import FeatureRequest
import shortuuid
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
import argparse

API_ROOT_URL = '/api/v1'

app = Flask(__name__)
test_mode = False

# Client app serve static files for HTML index and app.js (minified from Grunt)

@app.route('/')
def client_app_html():
    return app.send_static_file('index.html')

@app.route('/app.js')
def client_app_js():
    return app.send_static_file('app.min.js')

@app.route('/app.css')
def client_app_css():
    return app.send_static_file('app.min.css')

@app.route('/logo.png')
def client_app_l():
    return app.send_static_file('logo.png')


# API endpoints

# Retrieve all existing feature requests
@app.route(API_ROOT_URL + '/feature-request', methods=['GET'])
def feature_requests_all_read():
    try:
        feature_request = FeatureRequest(test=test_mode)
        feature_requests = feature_request.find_all()
        feature_requests_list = []
        for feature_request in feature_requests:
            feature_requests_list.append(feature_request.to_dict())
        return jsonify(feature_requests=feature_requests_list)
    except Exception, e:
        print e
        return e

# Retrieve a single feature request by ID
@app.route(API_ROOT_URL + '/feature-request/<feature_request_id>', methods=['GET'])
def feature_request_by_id_read(feature_request_id):
    try:
        feature_request = FeatureRequest(test=test_mode)
        feature_request = feature_request.find_by_id(feature_request_id)
        return jsonify(feature_request.to_dict())
    except Exception, e:
        print e
        return e

# Add a new feature request
@app.route(API_ROOT_URL + '/feature-request', methods=['POST'])
def feature_request_add():
    data = request.data
    data_dict = json.loads(data)
    feature_requests_dict = {}
    feature_request = FeatureRequest(test=test_mode)
    feature_request.title = data_dict['title']
    feature_request.description = data_dict['description']
    feature_request.client_name = data_dict['client_name']
    feature_request.client_priority = data_dict['client_priority']
    feature_request.target_date = data_dict['target_date']
    feature_request.product_area = data_dict['product_area']
    feature_request.agent_name = data_dict['agent_name']
    feature_request.save()
    return jsonify({
        'status': 'success',
        'message': 'Feature request added',
        'feature_request': feature_request.to_dict()
    })

# Update existing feature request
@app.route(API_ROOT_URL + '/feature-request/<feature_request_id>', methods=['PUT'])
def feature_requests_update(feature_request_id):
    try:
        data = request.data
        data_dict = json.loads(data)
        feature_requests_dict = {}
        feature_request = FeatureRequest(test=test_mode)
        feature_request.find_by_id(feature_request_id)
        try:
            feature_request.title = data_dict['title']
        except KeyError:
            pass
        try:
            feature_request.description = data_dict['description']
        except KeyError:
            pass
        try:
            feature_request.client_name = data_dict['client_name']
        except KeyError:
            pass
        try:
            feature_request.client_priority = data_dict['client_priority']
        except KeyError:
            pass
        try:
            feature_request.target_date = data_dict['target_date']
        except KeyError:
            pass
        try:
            feature_request.product_area = data_dict['product_area']
        except KeyError:
            pass
        try:
            feature_request.agent_name = data_dict['agent_name']
        except KeyError:
            pass
        try:
            feature_request.is_open = data_dict['is_open']
        except KeyError:
            pass
    except Exception, e:
        return e

    feature_request.save()
    return jsonify({
        'status': 'success',
        'message': 'Feature request updated',
        'feature_request': feature_request.to_dict()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint does not exist'
    }), 404

# When running from CLI, "--mode test" will use test db this is for selenium mostly
# When running from CLI, "--public" can be used to listen publicly in development environment (no apache, tornado, etc)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='dev')
    parser.add_argument('-p', '--public', default='false')
    args = vars(parser.parse_args())
    if args['mode'] == 'test':
        test_mode = True
    if args['public'] == 'true':
        app.run('0.0.0.0')
    else:
        app.run(debug=True)

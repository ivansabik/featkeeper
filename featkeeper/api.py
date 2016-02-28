# api.py
from flask import Flask, jsonify

API_ROOT_URL = '/api/v1'

app = Flask(__name__)

@app.route(API_ROOT_URL + '/feature-request', methods=['GET'])
def feature_requests_all_read():
    return jsonify({})

@app.route(API_ROOT_URL + '/feature-request/<feature_request_id>', methods=['GET'])
def feature_request_by_id_read(feature_request_id):
    return jsonify({})

@app.route(API_ROOT_URL + '/feature-request', methods=['PUT'])
def feature_request_add():
    return jsonify({})

@app.route(API_ROOT_URL + '/feature-request', methods=['POST'])
def feature_requests_update():
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return jsonify({ 'error': 'Endpoint does no texist' }), 404

if __name__ == "__main__":
    app.debug = True
    app.run()

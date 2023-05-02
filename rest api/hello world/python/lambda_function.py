import serverless_wsgi

from flask import Flask, jsonify


# the flask app
app = Flask(__name__)


# home route
@app.route('/', methods=['GET'])
def index():
    res = {
        'message': 'Hello World!'
    }

    return jsonify(res), 200


# ping route
@app.route('/ping', methods=['GET'])
def get_gats():
    res = {
        'success': True,
    }

    return jsonify(res), 200


# entry point
# parses the request and passes it to the flask app
def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

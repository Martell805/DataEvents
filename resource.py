from flask import Flask, jsonify
from flask_restful import reqparse, Resource
import json
from skill import main_skill

parser = reqparse.RequestParser()
parser.add_argument('session', required=True)
parser.add_argument('meta', required=True)
parser.add_argument('request', required=True)
parser.add_argument('version', required=True)


def form_request():
    args = parser.parse_args()
    ans = args.__repr__().replace('"', '').replace("'", '"').replace("True", "true").replace("False", "false")
    print(ans)
    return json.loads(ans)


class MyResource(Resource):
    def post(self):
        req = form_request()
        print(req)
        answer = {
            'session': {
                'session_id': req['session']['session_id'],
                'user_id': req['session']['user_id'],
                'message_id': req['session']['message_id']
            },
            'response': {
                'text': 'Hello world!',
                'end_session': False
            },
            'version': req['version']}

        answer = main_skill(req, answer)

        return jsonify(answer)

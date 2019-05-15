from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint

from config import Config

VERIFY_TOKEN=Config.VERIFY_TOKEN

# This is to verify for facebook using your verify token
@routes.route("/", methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"
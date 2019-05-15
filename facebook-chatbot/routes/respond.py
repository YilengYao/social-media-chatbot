from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint

from config import Config
from .watson_chatbot import WatsonChatbot

# Watson Chatbot API Credentials
version=Config.VERSION
username=Config.USERNAME 
password=Config.PASSWORD
url=Config.URL
workspace_id=Config.WORKSPACE_ID

# Facebook messenger credentials
VERIFY_TOKEN=Config.VERIFY_TOKEN
ACCESS_TOKEN=Config.ACCESS_TOKEN

chatbot = WatsonChatbot(version, username, password, url)

def reply(user_id, msg):
    """
    param: user_id - the user id of the person that send you a message on messenger
    param: msg - the message that we receive from chatbot and reply to messenger
    This function takes a message chatbot and send it back to the original facebook user that messaged the chatbot
    """
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(ACCESS_TOKEN)
    resp = requests.post(url, json=data)
    print(resp.content)


@routes.route("/", methods=['POST'])
def handle_incoming_messages():
    """
    Gets incoming messages from facebook messenger, send it to watson chatbot, after a response from watson chatbot, it is sent back to a function that handles replying back to facebook messenger.
    """
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, chatbot.chatbot_response(workspace_id, message))
    return "ok"


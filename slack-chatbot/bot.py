import os

from slackclient import SlackClient

from config import Config
from watson_chatbot import WatsonChatbot


# Watson Chatbot API Credentials
version=Config.VERSION
username=Config.USERNAME 
password=Config.PASSWORD
url=Config.URL
workspace_id=Config.WORKSPACE_ID

class Bot(object):
    """ Instantiates a Bot object to handle Slack onboarding interactions."""
    def __init__(self):
        super(Bot, self).__init__()
        self.name = "pythonboardingbot"
        self.emoji = ":robot_face:"
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        self.oauth = {"client_id": Config.CLIENT_ID,
                      "client_secret": Config.CLIENT_SECRET,
                      # Scopes provide and limit permissions to what our app
                      # can access. It's important to use the most restricted
                      # scope that your app will need.
                      "scope": "bot"}
        self.verification = Config.VERIFICATION_TOKEN
        self.slack_api_token = Config.SLACK_API_TOKEN

        # NOTE: Python-slack requires a client connection to generate
        # an OAuth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        self.client = SlackClient("")

        # create watson chatbot object to communicate with watson chatbot
        self.chatbot = WatsonChatbot(version, username, password, url)


    def reply(self, slack_event):
        # create slack client to reply on slack channel
        self.client = SlackClient(self.slack_api_token)

        try:
            user_id = slack_event["event"]["user"]
            channel = slack_event["event"]["channel"]
            message = slack_event["event"]["text"]
            # reply to user if it is a direct message
            if slack_event["event"]["channel_type"] == "im":
                response = self.chatbot.chatbot_response(workspace_id, message)
                self.client.api_call("chat.postMessage",
                                                channel=channel,
                                                user_id=user_id,
                                                text = response)
        except:
            return "cannot find user channel"

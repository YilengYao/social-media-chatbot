import os

class Config(object):
    # Slackbot credentials obtained at https://api.slack.com/apps -> basic information
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    VERIFICATION_TOKEN = ''
    # Slack API token abtained at https://api.slack.com/apps -> OAuth & Permissions Bot User OAuth Access Token
    SLACK_API_TOKEN = ''


    # Watson Chatbot API Credentials
    VERSION = ''
    USERNAME = ''
    PASSWORD = ''
    URL = 'https://gateway.watsonplatform.net/assistant/api'
    WORKSPACE_ID = ''
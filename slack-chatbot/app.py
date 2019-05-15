import bot
from flask import Flask, request, make_response, render_template, jsonify, Response 
import json 
import os 

pyBot = bot.Bot()
slack = pyBot.client


app = Flask( __name__, static_url_path='' )

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int( os.getenv( 'PORT', 8000 ) )


# This is a default hello world homepage, that will be display if your function runs properly
@app.route("/", methods=["GET", "POST"])
def hears():
    """
    This route listens for incoming events from Slack and uses the event
    handler helper function to route events to our Bot.
    """
    print("listening")
    slack_event = request.get_json()
    print(slack_event)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                        "application/json"
                                                            })
    try:
        if slack_event["event"]["subtype"] == 'bot_message':
            return "chatbot reply"
    except:
        pyBot.reply(slack_event)

    return 'Aready'

# This is the entry point of your app
if __name__ == '__main__':
    print(port)
    app.run( host='0.0.0.0', port=8000, debug=True)
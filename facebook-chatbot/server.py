from flask import Flask, request, jsonify, Response
import json
import os
from routes import *

app = Flask( __name__, static_url_path='' )

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int( os.getenv( 'PORT', 8000 ) )

app.register_blueprint(routes)

# This is a default hello world homepage, that will be display if your function runs properly
@app.route('/')
def hello_world():
    return 'Hello, World!'

# This is the entry point of your app
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=port, debug=True)
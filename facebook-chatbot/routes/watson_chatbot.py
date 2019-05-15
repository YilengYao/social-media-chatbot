from ibm_watson import AssistantV1
import json

# This is a wrapper for us to talk to Watson Chatbot API
class WatsonChatbot:

    def __init__(self, version, username, password, url):
        """
        This function creates a watson assistant object that allows us to talk to watson chatbot
        param: version - version of watson assistant
        param: username - username of your watson assistant
        param: password - password of your watson assistant
        param: url - the url of your watson assistant service, to find go to
        https://cloud.ibm.com/resources, go to Services, click on Watson Assistant
        """
        self.assistant = AssistantV1(
            version=version,
            username=username,
            password=password,
            url=url
        )

    def chatbot_response(self, workspace_id, message):
        """
        This function is used to talk to watson chatbot, first we send a message to watson assistent and in return get a response.
        param: workspace_id - workspace id of watson assistant
        param: message - the message you want to send to your watson chatbot

        Returns message from watson chatbot
        """
        response = self.assistant.message(
            workspace_id=workspace_id,
            input={
                'text': message
            }
        ).get_result()
        return response['output']['text'][0]
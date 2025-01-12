from typing import Dict, Callable, Union, Any

from slack_bolt import App

from slack.handlers.added_message_handler import AddedMessageHandler
from slack.listeners.listenable import Listenable
from slack.listeners.message.slack_message_response_params import SlackMessageResponseParams


class AddedMessageListener(Listenable):

    def __init__(self, message_handler: AddedMessageHandler):
        self.message_handler = message_handler

    def added_message(self, message, say: Callable[[Union[str, Dict[str, Any]]], None]):
        if message:
            message_event = SlackMessageResponseParams(**message)
            client_response = self.message_handler.handel_message(message_event)
            say(client_response)

    def listen(self, app: App):
        app.message()(self.added_message)

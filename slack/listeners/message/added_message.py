from typing import List, Dict

from slack_bolt import App

from llm_service.llm_client import LLMClient
from slack.listeners.listenable import Listenable


class AddedMessage(Listenable):

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": "You are a intelligent assistant."
            }
        ]

    def added_message(self, message, say):
        if message:
            self.messages.append(
                {"role": "user", "content": message["text"]},
            )
            response = self.llm_client.send_message_request(self.messages)

            # self.messages.append({"role": "assistant"}) # TODO: add the assistant answer - response.content
            say(response.content)

    def listen(self, app: App):
        app.message()(self.added_message)

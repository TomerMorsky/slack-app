from typing import List, Dict

from slack_bolt import App

from slack.listeners.listenable import Listenable


class AddedMessage(Listenable):

    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": "You are a intelligent assistant."
            }
        ]

    @staticmethod
    def added_message(message, say):
        if message:
            # message.append(
            #     {"role": "user", "content": message["text"]},
            # )
            # response = llm_client.send_message_request(message)
            # response_message = response.content
            #
            # message.append({"role": "assistant"})

            #     if message:
            #         # message.append(
            #         #     {"role": "user", "content": message["text"]},
            #         # )
            #         # response = llm_client.send_message_request(message)
            #         # response_message = response.content
            #         #
            #         # message.append({"role": "assistant"})
            #         say("Your message is: " + message["text"] + " your reply is: " + "response_message")
            say("Your message is: " + message["text"] + " your reply is: " + "response_message")

    def listen(self, app: App):
        app.message()(self.added_message)

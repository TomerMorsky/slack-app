from slack_bolt import App

from slack.listeners.message import added_message


class SlackListeners:
    def __init__(self, app: App):
        self.app = app

    def register_listeners(self):
        added_message.listen(self.app)

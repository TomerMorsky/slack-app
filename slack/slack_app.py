from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from config.config import SlackConfig
from slack.listeners.slack_listeners import SlackListeners


class SlackApp:
    def __init__(self, slack_config: SlackConfig):
        self.config = slack_config

    def start_slack_app(self):
        app = App(token=self.config.bot_token, name="Hw Bot")
        slack_listeners = SlackListeners(app)
        slack_listeners.register_listeners()
        handler = SocketModeHandler(app, self.config.app_token)
        handler.start()

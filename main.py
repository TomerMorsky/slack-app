from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config.open_ai_config import open_ai_config
from config.slack_config import slack_config
from open_ai.open_ai_client import OpenAIClient
from open_ai.open_ai_model import OpenAIModel

from slack.listeners.slack_listeners import SlackListeners


def main():
    load_dotenv()

    app = App(token=slack_config.slack_bot_token, name="Hw Bot")
    slack_listeners = SlackListeners(app)
    slack_listeners.register_listeners()

    llm_client = OpenAIClient(open_ai_config.api_key, OpenAIModel.gpt_4o_mini)
    handler = SocketModeHandler(app, slack_config.slack_app_token)
    handler.start()


if __name__ == "__main__":
    main()

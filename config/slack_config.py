import os

from config.config import SlackConfig

slack_config = SlackConfig(
    slack_bot_token=os.getenv("SLACK_BOT_TOKEN"),
    slack_app_token=os.getenv("SLACK_APP_TOKEN")
)

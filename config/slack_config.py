import os

from config.config import SlackConfig

slack_config = SlackConfig(
    bot_token=os.getenv("SLACK_BOT_TOKEN"),
    app_token=os.getenv("SLACK_APP_TOKEN")
)

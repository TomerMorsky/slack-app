from pydantic import BaseModel


class SlackConfig(BaseModel):
    slack_bot_token: str
    slack_app_token: str


class OpenAIConfig(BaseModel):
    api_key: str

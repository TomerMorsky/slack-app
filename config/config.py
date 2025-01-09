from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class SlackConfig(BaseModel):
    bot_token: str
    app_token: str


class OpenAIConfig(BaseModel):
    api_key: str

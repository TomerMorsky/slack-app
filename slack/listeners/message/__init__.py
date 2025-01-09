from config.open_ai_config import open_ai_config
from open_ai.open_ai_client import OpenAIClient
from open_ai.open_ai_model import OpenAIModel
from slack.listeners.message.added_message import AddedMessage

added_message = AddedMessage(OpenAIClient(open_ai_config.api_key, OpenAIModel.gpt_4o_mini))

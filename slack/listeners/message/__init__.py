from config.open_ai_config import open_ai_config
from open_ai.open_ai_client import OpenAIClient
from open_ai.open_ai_model import OpenAIModel
from slack.handlers.added_message_handler import AddedMessageHandler
from slack.listeners.message.added_message_listener import AddedMessageListener

added_message_handler = AddedMessageHandler(OpenAIClient(open_ai_config.api_key, OpenAIModel.gpt_4o_mini))
added_message = AddedMessageListener(added_message_handler)

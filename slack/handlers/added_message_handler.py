from typing import List, Dict

from llm_service.llm_client import LLMClient
from llm_service.types.llm_message import LLMMessage
from mongo.mongo_client import MongoDBClient
from mongo.types.slack_message import SlackMessage
from slack.listeners.message.slack_message_response_params import SlackMessageResponseParams


class AddedMessageHandler:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.mongo_client = MongoDBClient()
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": "You are an intelligent assistant."
            }
        ]

    def handel_message(self, message: SlackMessageResponseParams) -> str:
        # TODO: get user messages (previous chat context)
        user_chat = self.mongo_client.get_user_chat(message.user)
        chat_messages = user_chat.messages

        new_message = SlackMessage(
            role="user",
            content=message.text,
            timestamp=message.ts,
            slack_message_id=message.client_msg_id
        )

        chat_messages.append(new_message)
        llm_messages = self.chat_message_to_llm_message(chat_messages)
        response = self.llm_client.send_message_request(llm_messages)

        new_assistant_message = SlackMessage(
            role="assistant",
            content=response.content,
            timestamp=response.created,
            slack_message_id=None
        )

        chat_messages.append(new_assistant_message)

        # self.messages.append({"role": "assistant", "content": response.content})
        user_chat.messages = chat_messages
        self.mongo_client.create_or_update_user_messages(user_chat)

        return response.content

    @staticmethod
    def chat_message_to_llm_message(chat_messages: List[SlackMessage]) -> List[LLMMessage]:
        llm_messages = []

        for chat_message in chat_messages:
            llm_message = LLMMessage(
                role=chat_message.role,
                content=chat_message.content
            )
            llm_messages.append(llm_message)

        return llm_messages

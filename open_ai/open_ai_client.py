from typing import List

from openai import OpenAI

from llm_service.llm_client import LLMClient
from llm_service.llm_message_response import LLMMessageResponse
from open_ai.open_ai_model import OpenAIModel


class OpenAIClient(LLMClient):
    def __init__(self, api_key: str, model_name: OpenAIModel):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def send_message_request(self, messages: List[dict]) -> LLMMessageResponse:
        response = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        last_message_from_open_ai = response.choices[0].message

        llm_message_response = LLMMessageResponse(
            id=response.id,
            created=response.created,
            model=response.model,
            content=last_message_from_open_ai
        )
        return llm_message_response

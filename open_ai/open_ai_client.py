from typing import List

from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

from llm_service.llm_client import LLMClient
from llm_service.llm_message_response import LLMMessageResponse
from open_ai.open_ai_model import OpenAIModel


class OpenAIClient(LLMClient):
    def __init__(self, api_key: str, model_name: OpenAIModel):
        self.client = OpenAI(api_key=api_key)
        self.model_name: str = model_name.value

    def send_message_request(self, messages: List[dict]) -> LLMMessageResponse:
        response = self.client.chat.completions.create(model=self.model_name, messages=messages)
        last_message_from_open_ai: ChatCompletionMessage = response.choices[0].message

        llm_message_response = LLMMessageResponse(
            id=response.id,
            created=response.created,
            model=response.model,
            content=last_message_from_open_ai.content
        )
        return llm_message_response

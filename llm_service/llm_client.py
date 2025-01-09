from abc import ABC, abstractmethod

from llm_service.llm_message_response import LLMMessageResponse


class LLMClient(ABC):

    @abstractmethod
    def send_message_request(self, messages: dict) -> LLMMessageResponse:
        pass

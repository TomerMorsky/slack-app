from abc import ABC, abstractmethod
from typing import List

from llm_service.llm_message_response import LLMMessageResponse


class LLMClient(ABC):

    @abstractmethod
    def send_message_request(self, messages:  List[dict]) -> LLMMessageResponse:
        pass

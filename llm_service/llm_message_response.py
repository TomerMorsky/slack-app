from dataclasses import dataclass


@dataclass
class LLMMessageResponse:
    id: str
    created: int
    model: str
    content: str

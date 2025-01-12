from typing import List, Optional

from pydantic import BaseModel

from mongo.types.slack_message import SlackMessage


class Chat(BaseModel):
    user: str
    messages: List[SlackMessage]
    chat_id: Optional[str]

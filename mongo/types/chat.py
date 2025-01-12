from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel

from mongo.types.slack_message import SlackMessage


class Chat(BaseModel):
    # _id: ObjectId
    user: str
    messages: List[SlackMessage]
    chat_id: Optional[str]

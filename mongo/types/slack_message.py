from typing import Optional

from pydantic import BaseModel


class SlackMessage(BaseModel):
    role: str
    content: str
    timestamp: str
    slack_message_id: Optional[str]

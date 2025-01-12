from pydantic import BaseModel, Extra


class SlackMessageResponseParams(BaseModel):
    user: str
    ts: str
    text: str
    client_msg_id: str
    channel: str

    class Config:
        extra = Extra.ignore

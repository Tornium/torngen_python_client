import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .user_message_id import UserMessageId
from .user_message_type_enum import UserMessageTypeEnum


@dataclass
class UserMessage(BaseSchema):
    """
    JSON object of `UserMessage`.
    """

    type: UserMessageTypeEnum
    topic: str
    timestamp: int
    sender: BasicUser
    seen: bool
    read: bool
    id: UserMessageId

    @staticmethod
    def parse(data):
        return UserMessage(
            type=BaseSchema.parse(data.get("type"), UserMessageTypeEnum),
            topic=BaseSchema.parse(data.get("topic"), str),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            sender=BaseSchema.parse(data.get("sender"), BasicUser),
            seen=BaseSchema.parse(data.get("seen"), bool),
            read=BaseSchema.parse(data.get("read"), bool),
            id=BaseSchema.parse(data.get("id"), UserMessageId),
        )

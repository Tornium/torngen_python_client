import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_event_id import UserEventId


@dataclass
class UserEvent(BaseSchema):
    """
    JSON object of `UserEvent`.
    """

    timestamp: int
    id: UserEventId
    event: str

    @staticmethod
    def parse(data):
        return UserEvent(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), UserEventId),
            event=BaseSchema.parse(data.get("event"), str),
        )

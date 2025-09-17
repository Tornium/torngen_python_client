import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_event import UserEvent


@dataclass
class UserNewEventsResponse(BaseSchema):
    """
    JSON object of `UserNewEventsResponse`.
    """

    events: typing.List[UserEvent]

    @staticmethod
    def parse(data):
        return UserNewEventsResponse(
            events=BaseSchema.parse(data.get("events"), typing.List[UserEvent]),
        )

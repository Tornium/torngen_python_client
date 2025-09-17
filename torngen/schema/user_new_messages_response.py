import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_message import UserMessage


@dataclass
class UserNewMessagesResponse(BaseSchema):
    """
    JSON object of `UserNewMessagesResponse`.
    """

    messages: typing.List[UserMessage]

    @staticmethod
    def parse(data):
        return UserNewMessagesResponse(
            messages=BaseSchema.parse(data.get("messages"), typing.List[UserMessage]),
        )

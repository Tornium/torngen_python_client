import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_message import UserMessage


@dataclass
class UserMessagesResponse(BaseSchema):
    """
    JSON object of `UserMessagesResponse`.
    """

    messages: typing.List[UserMessage]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserMessagesResponse(
            messages=BaseSchema.parse(data.get("messages"), typing.List[UserMessage]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

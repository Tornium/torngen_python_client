import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_event import UserEvent


@dataclass
class UserEventsResponse(BaseSchema):
    """
    JSON object of `UserEventsResponse`.
    """

    events: typing.List[UserEvent]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserEventsResponse(
            events=BaseSchema.parse(data.get("events"), typing.List[UserEvent]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

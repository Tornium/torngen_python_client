import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_display import UserDisplay


@dataclass
class UserDisplayResponse(BaseSchema):
    """
    JSON object of `UserDisplayResponse`.
    """

    display: UserDisplay
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserDisplayResponse(
            display=BaseSchema.parse(data.get("display"), UserDisplay),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_bazaar import UserBazaar


@dataclass
class UserBazaarResponse(BaseSchema):
    """
    JSON object of `UserBazaarResponse`.
    """

    bazaar: UserBazaar
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserBazaarResponse(
            bazaar=BaseSchema.parse(data.get("bazaar"), UserBazaar),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

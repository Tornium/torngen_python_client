import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal
from .user_search import UserSearch


@dataclass
class UserSearchResponse(BaseSchema):
    """
    JSON object of `UserSearchResponse`.
    """

    search: typing.List[UserSearch]
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return UserSearchResponse(
            search=BaseSchema.parse(data.get("search"), typing.List[UserSearch]),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

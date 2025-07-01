import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_list import UserList


@dataclass
class UserListResponse(BaseSchema):
    """
    JSON object of `UserListResponse`.
    """

    list: typing.List[UserList]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserListResponse(
            list=BaseSchema.parse(data.get("list"), typing.List[UserList]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

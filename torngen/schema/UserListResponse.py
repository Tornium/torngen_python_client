import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from UserList import UserList

from ..base_schema import BaseSchema


class UserListResponse(BaseSchema):

    list: typing.List[UserList]
    _metadata: RequestMetadataWithLinks

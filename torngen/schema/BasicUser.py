import typing

from UserId import UserId

from ..base_schema import BaseSchema


class BasicUser(BaseSchema):

    name: str
    id: UserId

import typing

from UserId import UserId

from ..base_schema import BaseSchema


class Bazaar(BaseSchema):

    name: str
    is_open: bool
    id: UserId

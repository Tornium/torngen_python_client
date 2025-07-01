import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionContributor(BaseSchema):

    value: int
    username: str
    in_faction: bool
    id: UserId

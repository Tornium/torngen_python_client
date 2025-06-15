import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionSearchLeader(BaseSchema):

    name: str
    id: UserId

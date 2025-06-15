import typing

from ..base_schema import BaseSchema


class FactionRank(BaseSchema):

    wins: int
    position: int
    name: str
    level: int
    division: int

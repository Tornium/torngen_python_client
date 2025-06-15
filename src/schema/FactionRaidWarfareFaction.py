import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionRaidWarfareFaction(BaseSchema):

    score: int | float
    name: str
    id: FactionId
    chain: int

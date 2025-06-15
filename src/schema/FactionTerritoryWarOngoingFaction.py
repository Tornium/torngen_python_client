import typing

from FactionId import FactionId
from UserId import UserId

from ..base_schema import BaseSchema


class FactionTerritoryWarOngoingFaction(BaseSchema):

    score: int
    playerIds: typing.List[UserId]
    name: str
    is_aggressor: bool
    id: FactionId
    chain: int

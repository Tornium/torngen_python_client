import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionTerritoryWarFaction(BaseSchema):

    score: int
    players_on_wall: typing.List[typing.Any]
    name: str
    id: FactionId
    chain: int

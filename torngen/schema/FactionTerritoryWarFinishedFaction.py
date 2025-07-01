import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionTerritoryWarFinishedFaction(BaseSchema):

    score: int
    name: str
    is_aggressor: bool
    id: FactionId

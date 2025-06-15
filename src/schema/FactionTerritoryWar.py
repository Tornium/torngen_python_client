import typing

from FactionId import FactionId
from FactionTerritoryWarParticipant import FactionTerritoryWarParticipant

from ..base_schema import BaseSchema


class FactionTerritoryWar(BaseSchema):

    winner: None | FactionId
    war_id: int
    territory: str
    target: int
    start: int
    factions: typing.List[FactionTerritoryWarParticipant]
    end: None | int

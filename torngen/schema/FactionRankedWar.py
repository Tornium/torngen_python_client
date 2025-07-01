import typing

from FactionRankedWarParticipant import FactionRankedWarParticipant

from ..base_schema import BaseSchema


class FactionRankedWar(BaseSchema):

    winner: None | int
    war_id: int
    target: int
    start: int
    factions: typing.List[FactionRankedWarParticipant]
    end: None | int

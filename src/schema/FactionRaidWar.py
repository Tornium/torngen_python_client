import typing

from FactionRaidWarParticipant import FactionRaidWarParticipant

from ..base_schema import BaseSchema


class FactionRaidWar(BaseSchema):

    war_id: int
    start: int
    factions: typing.List[FactionRaidWarParticipant]
    end: None | int

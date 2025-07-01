import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_war_participant import FactionRaidWarParticipant


@dataclass
class FactionRaidWar(BaseSchema):
    """
    JSON object of `FactionRaidWar`.
    """

    war_id: int
    start: int
    factions: typing.List[FactionRaidWarParticipant]
    end: None | int

    @staticmethod
    def parse(data):
        return FactionRaidWar(
            war_id=BaseSchema.parse(data.get("war_id"), int),
            start=BaseSchema.parse(data.get("start"), int),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionRaidWarParticipant]
            ),
            end=BaseSchema.parse(data.get("end"), None | int),
        )

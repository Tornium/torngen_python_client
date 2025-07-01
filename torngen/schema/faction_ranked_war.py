import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_ranked_war_participant import FactionRankedWarParticipant


@dataclass
class FactionRankedWar(BaseSchema):
    """
    JSON object of `FactionRankedWar`.
    """

    winner: None | int
    war_id: int
    target: int
    start: int
    factions: typing.List[FactionRankedWarParticipant]
    end: None | int

    @staticmethod
    def parse(data):
        return FactionRankedWar(
            winner=BaseSchema.parse(data.get("winner"), None | int),
            war_id=BaseSchema.parse(data.get("war_id"), int),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionRankedWarParticipant]
            ),
            end=BaseSchema.parse(data.get("end"), None | int),
        )

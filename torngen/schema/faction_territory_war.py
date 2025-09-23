import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_territory_war_participant import FactionTerritoryWarParticipant


@dataclass
class FactionTerritoryWar(BaseSchema):
    """
    JSON object of `FactionTerritoryWar`.
    """

    winner: typing.Optional[None | FactionId]
    war_id: int
    territory: str
    target: int
    start: int
    factions: typing.List[FactionTerritoryWarParticipant]
    end: None | int

    @staticmethod
    def parse(data):
        return FactionTerritoryWar(
            winner=BaseSchema.parse(
                data.get("winner"), typing.Optional[None | FactionId]
            ),
            war_id=BaseSchema.parse(data.get("war_id"), int),
            territory=BaseSchema.parse(data.get("territory"), str),
            target=BaseSchema.parse(data.get("target"), int),
            start=BaseSchema.parse(data.get("start"), int),
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[FactionTerritoryWarParticipant]
            ),
            end=BaseSchema.parse(data.get("end"), None | int),
        )

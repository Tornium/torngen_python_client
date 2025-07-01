import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_war import FactionRaidWar
from .faction_ranked_war import FactionRankedWar
from .faction_territory_war import FactionTerritoryWar


@dataclass
class FactionWars(BaseSchema):
    """
    JSON object of `FactionWars`.
    """

    territory: typing.List[FactionTerritoryWar]
    ranked: None | FactionRankedWar
    raids: typing.List[FactionRaidWar]

    @staticmethod
    def parse(data):
        return FactionWars(
            territory=BaseSchema.parse(
                data.get("territory"), typing.List[FactionTerritoryWar]
            ),
            ranked=BaseSchema.parse(data.get("ranked"), None | FactionRankedWar),
            raids=BaseSchema.parse(data.get("raids"), typing.List[FactionRaidWar]),
        )

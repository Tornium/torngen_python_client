import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_war_finished import FactionTerritoryWarFinished


@dataclass
class FactionTerritoryWarsHistoryResponse(BaseSchema):
    """
    JSON object of `FactionTerritoryWarsHistoryResponse`.
    """

    territorywars: typing.List[FactionTerritoryWarFinished]

    @staticmethod
    def parse(data):
        return FactionTerritoryWarsHistoryResponse(
            territorywars=BaseSchema.parse(
                data.get("territorywars"), typing.List[FactionTerritoryWarFinished]
            ),
        )

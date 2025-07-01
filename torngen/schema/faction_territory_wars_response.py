import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_war_finished import FactionTerritoryWarFinished
from .faction_territory_war_ongoing import FactionTerritoryWarOngoing


@dataclass
class FactionTerritoryWarsResponse(BaseSchema):
    """
    JSON object of `FactionTerritoryWarsResponse`.
    """

    territorywars: (
        typing.List[FactionTerritoryWarFinished]
        | typing.List[FactionTerritoryWarOngoing]
    )

    @staticmethod
    def parse(data):
        return FactionTerritoryWarsResponse(
            territorywars=BaseSchema.parse(
                data.get("territorywars"),
                typing.List[FactionTerritoryWarFinished]
                | typing.List[FactionTerritoryWarOngoing],
            ),
        )

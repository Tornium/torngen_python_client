import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_war_report import FactionTerritoryWarReport


@dataclass
class FactionTerritoryWarReportResponse(BaseSchema):
    """
    JSON object of `FactionTerritoryWarReportResponse`.
    """

    territorywarreport: typing.List[FactionTerritoryWarReport]

    @staticmethod
    def parse(data):
        return FactionTerritoryWarReportResponse(
            territorywarreport=BaseSchema.parse(
                data.get("territorywarreport"), typing.List[FactionTerritoryWarReport]
            ),
        )

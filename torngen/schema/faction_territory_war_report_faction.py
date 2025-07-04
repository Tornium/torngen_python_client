import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_territory_war_report_members import FactionTerritoryWarReportMembers


@dataclass
class FactionTerritoryWarReportFaction(BaseSchema):
    """
    JSON object of `FactionTerritoryWarReportFaction`.
    """

    score: int
    name: str
    members: typing.List[FactionTerritoryWarReportMembers]
    joins: int
    is_aggressor: bool
    id: FactionId
    clears: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarReportFaction(
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), str),
            members=BaseSchema.parse(
                data.get("members"), typing.List[FactionTerritoryWarReportMembers]
            ),
            joins=BaseSchema.parse(data.get("joins"), int),
            is_aggressor=BaseSchema.parse(data.get("is_aggressor"), bool),
            id=BaseSchema.parse(data.get("id"), FactionId),
            clears=BaseSchema.parse(data.get("clears"), int),
        )

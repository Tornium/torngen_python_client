import typing

from FactionId import FactionId
from FactionTerritoryWarReportMembers import FactionTerritoryWarReportMembers

from ..base_schema import BaseSchema


class FactionTerritoryWarReportFaction(BaseSchema):

    score: int
    name: str
    members: typing.List[FactionTerritoryWarReportMembers]
    joins: int
    is_aggressor: bool
    id: FactionId
    clears: int

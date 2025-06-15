import typing

from FactionTerritoryWarReport import FactionTerritoryWarReport

from ..base_schema import BaseSchema


class FactionTerritoryWarReportResponse(BaseSchema):

    territorywarreport: typing.List[FactionTerritoryWarReport]

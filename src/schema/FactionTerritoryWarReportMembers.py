import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionTerritoryWarReportMembers(BaseSchema):

    username: str
    score: int
    level: int
    joins: int
    id: UserId
    clears: int

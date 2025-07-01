import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionTerritoryWarReportMembers(BaseSchema):
    """
    JSON object of `FactionTerritoryWarReportMembers`.
    """

    username: str
    score: int
    level: int
    joins: int
    id: UserId
    clears: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarReportMembers(
            username=BaseSchema.parse(data.get("username"), str),
            score=BaseSchema.parse(data.get("score"), int),
            level=BaseSchema.parse(data.get("level"), int),
            joins=BaseSchema.parse(data.get("joins"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            clears=BaseSchema.parse(data.get("clears"), int),
        )

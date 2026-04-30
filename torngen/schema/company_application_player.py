import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_application_player_stats import CompanyApplicationPlayerStats
from .user_id import UserId


@dataclass
class CompanyApplicationPlayer(BaseSchema):
    """
    JSON object of `CompanyApplicationPlayer`.
    """

    stats: CompanyApplicationPlayerStats
    name: str
    level: int
    id: UserId

    @staticmethod
    def parse(data):
        return CompanyApplicationPlayer(
            stats=BaseSchema.parse(data.get("stats"), CompanyApplicationPlayerStats),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

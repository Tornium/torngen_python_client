import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionTerritoryWarFactionWallPlayers(BaseSchema):
    """
    JSON object of `FactionTerritoryWarFactionWallPlayers`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return FactionTerritoryWarFactionWallPlayers(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

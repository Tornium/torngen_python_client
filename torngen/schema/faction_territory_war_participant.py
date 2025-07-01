import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_id import UserId


@dataclass
class FactionTerritoryWarParticipant(BaseSchema):
    """
    JSON object of `FactionTerritoryWarParticipant`.
    """

    score: int
    playerIds: typing.List[UserId]
    name: str
    is_aggressor: bool
    id: FactionId
    chain: int

    @staticmethod
    def parse(data):
        return FactionTerritoryWarParticipant(
            score=BaseSchema.parse(data.get("score"), int),
            playerIds=BaseSchema.parse(data.get("playerIds"), typing.List[UserId]),
            name=BaseSchema.parse(data.get("name"), str),
            is_aggressor=BaseSchema.parse(data.get("is_aggressor"), bool),
            id=BaseSchema.parse(data.get("id"), FactionId),
            chain=BaseSchema.parse(data.get("chain"), int),
        )

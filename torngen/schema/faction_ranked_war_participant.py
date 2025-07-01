import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionRankedWarParticipant(BaseSchema):
    """
    JSON object of `FactionRankedWarParticipant`.
    """

    score: int
    name: str
    id: FactionId
    chain: int

    @staticmethod
    def parse(data):
        return FactionRankedWarParticipant(
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            chain=BaseSchema.parse(data.get("chain"), int),
        )

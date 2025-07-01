import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionRaidWarParticipant(BaseSchema):
    """
    JSON object of `FactionRaidWarParticipant`.
    """

    score: int
    name: str
    is_aggressor: bool
    id: FactionId
    chain: int

    @staticmethod
    def parse(data):
        return FactionRaidWarParticipant(
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_aggressor=BaseSchema.parse(data.get("is_aggressor"), bool),
            id=BaseSchema.parse(data.get("id"), FactionId),
            chain=BaseSchema.parse(data.get("chain"), int),
        )

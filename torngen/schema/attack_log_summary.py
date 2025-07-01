import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class AttackLogSummary(BaseSchema):
    """
    JSON object of `AttackLogSummary`.
    """

    name: None | str
    misses: int
    id: None | UserId
    hits: int
    damage: int

    @staticmethod
    def parse(data):
        return AttackLogSummary(
            name=BaseSchema.parse(data.get("name"), None | str),
            misses=BaseSchema.parse(data.get("misses"), int),
            id=BaseSchema.parse(data.get("id"), None | UserId),
            hits=BaseSchema.parse(data.get("hits"), int),
            damage=BaseSchema.parse(data.get("damage"), int),
        )

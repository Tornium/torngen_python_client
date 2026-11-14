import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class AttackLogDefender(BaseSchema):
    """
    JSON object of `AttackLogDefender`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return AttackLogDefender(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

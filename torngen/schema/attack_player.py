import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_faction_basic import UserFactionBasic
from .user_id import UserId


@dataclass
class AttackPlayer(BaseSchema):
    """
    JSON object of `AttackPlayer`.
    """

    name: str
    level: int
    id: UserId
    faction: None | UserFactionBasic

    @staticmethod
    def parse(data):
        return AttackPlayer(
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            faction=BaseSchema.parse(data.get("faction"), None | UserFactionBasic),
        )

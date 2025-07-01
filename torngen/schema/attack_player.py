import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_player_faction import AttackPlayerFaction
from .user_id import UserId


@dataclass
class AttackPlayer(BaseSchema):
    """
    JSON object of `AttackPlayer`.
    """

    name: str
    level: int
    id: UserId
    faction: None | AttackPlayerFaction

    @staticmethod
    def parse(data):
        return AttackPlayer(
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            faction=BaseSchema.parse(data.get("faction"), None | AttackPlayerFaction),
        )

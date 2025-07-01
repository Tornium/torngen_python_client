import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_id import UserId


@dataclass
class AttackPlayerSimplified(BaseSchema):
    """
    JSON object of `AttackPlayerSimplified`.
    """

    id: UserId
    faction_id: None | FactionId

    @staticmethod
    def parse(data):
        return AttackPlayerSimplified(
            id=BaseSchema.parse(data.get("id"), UserId),
            faction_id=BaseSchema.parse(data.get("faction_id"), None | FactionId),
        )

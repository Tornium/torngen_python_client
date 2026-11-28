import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_log_item import AttackLogItem
from .user_id import UserId


@dataclass
class AttackLogAttacker(BaseSchema):
    """
    JSON object of `AttackLogAttacker`.
    """

    name: str
    item: None | AttackLogItem
    id: UserId

    @staticmethod
    def parse(data):
        return AttackLogAttacker(
            name=BaseSchema.parse(data.get("name"), str),
            item=BaseSchema.parse(data.get("item"), None | AttackLogItem),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

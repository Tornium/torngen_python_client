import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class AttackLogItem(BaseSchema):
    """
    JSON object of `AttackLogItem`.
    """

    name: str
    id: ItemId

    @staticmethod
    def parse(data):
        return AttackLogItem(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )

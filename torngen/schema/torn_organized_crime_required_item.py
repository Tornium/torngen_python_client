import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class TornOrganizedCrimeRequiredItem(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeRequiredItem`.
    """

    name: str
    is_used: bool
    id: ItemId

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeRequiredItem(
            name=BaseSchema.parse(data.get("name"), str),
            is_used=BaseSchema.parse(data.get("is_used"), bool),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )

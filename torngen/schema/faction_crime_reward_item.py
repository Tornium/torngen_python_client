import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class FactionCrimeRewardItem(BaseSchema):
    """
    JSON object of `FactionCrimeRewardItem`.
    """

    quantity: int
    id: ItemId

    @staticmethod
    def parse(data):
        return FactionCrimeRewardItem(
            quantity=BaseSchema.parse(data.get("quantity"), int),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ItemMarketListingStackable(BaseSchema):
    """
    JSON object of `ItemMarketListingStackable`.
    """

    price: int
    amount: int

    @staticmethod
    def parse(data):
        return ItemMarketListingStackable(
            price=BaseSchema.parse(data.get("price"), int),
            amount=BaseSchema.parse(data.get("amount"), int),
        )

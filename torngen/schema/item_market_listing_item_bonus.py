import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ItemMarketListingItemBonus(BaseSchema):
    """
    JSON object of `ItemMarketListingItemBonus`.
    """

    value: int
    title: str
    id: int
    description: str

    @staticmethod
    def parse(data):
        return ItemMarketListingItemBonus(
            value=BaseSchema.parse(data.get("value"), int),
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), int),
            description=BaseSchema.parse(data.get("description"), str),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ItemMarketListingItemStats(BaseSchema):
    """
    JSON object of `ItemMarketListingItemStats`.
    """

    quality: int | float
    damage: None | int | float
    armor: None | int | float
    accuracy: None | int | float

    @staticmethod
    def parse(data):
        return ItemMarketListingItemStats(
            quality=BaseSchema.parse(data.get("quality"), int | float),
            damage=BaseSchema.parse(data.get("damage"), None | int | float),
            armor=BaseSchema.parse(data.get("armor"), None | int | float),
            accuracy=BaseSchema.parse(data.get("accuracy"), None | int | float),
        )

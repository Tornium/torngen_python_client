import typing

from ..base_schema import BaseSchema


class ItemMarketListingItemStats(BaseSchema):

    quality: int | float
    damage: None | int | float
    armor: None | int | float
    accuracy: None | int | float

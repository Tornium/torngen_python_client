import typing

from ItemMarketListingItemBonus import ItemMarketListingItemBonus
from ItemMarketListingItemStats import ItemMarketListingItemStats
from ItemUid import ItemUid

from ..base_schema import BaseSchema


class ItemMarketListingItemDetails(BaseSchema):

    uid: ItemUid
    stats: ItemMarketListingItemStats
    rarity: None | str
    bonuses: typing.List[ItemMarketListingItemBonus]

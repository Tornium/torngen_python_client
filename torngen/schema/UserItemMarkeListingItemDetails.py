import typing

from ItemMarketListingItemBonus import ItemMarketListingItemBonus
from ItemMarketListingItemStats import ItemMarketListingItemStats
from ItemUid import ItemUid

from ..base_schema import BaseSchema


class UserItemMarkeListingItemDetails(BaseSchema):

    uid: None | ItemUid
    type: str
    stats: None | ItemMarketListingItemStats
    rarity: None | str
    name: str
    id: int
    bonuses: typing.List[ItemMarketListingItemBonus]

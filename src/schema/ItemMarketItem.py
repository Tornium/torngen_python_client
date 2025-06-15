import typing

from ItemId import ItemId

from ..base_schema import BaseSchema


class ItemMarketItem(BaseSchema):

    type: str
    name: str
    id: ItemId
    average_price: int

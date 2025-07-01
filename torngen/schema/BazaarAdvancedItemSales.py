import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarAdvancedItemSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"advanced_item_sales": int}) | Bazaar]

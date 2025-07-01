import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarAdvancedItemSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"advanced_item_sales": int}) | Bazaar]

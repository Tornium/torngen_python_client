import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarBulkSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"bulk_sales": int}) | Bazaar]

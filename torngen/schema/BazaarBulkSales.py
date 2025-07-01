import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarBulkSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"bulk_sales": int}) | Bazaar]

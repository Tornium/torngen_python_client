import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarDollarSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"dollar_sales": int}) | Bazaar]

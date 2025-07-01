import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarDollarSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"dollar_sales": int}) | Bazaar]

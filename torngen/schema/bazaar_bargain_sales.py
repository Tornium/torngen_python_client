import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarBargainSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"bargain_sales": int}) | Bazaar]

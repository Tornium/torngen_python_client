import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarBargainSales(BaseSchema):
    value: typing.List[typing.TypedDict("", {"bargain_sales": int}) | Bazaar]

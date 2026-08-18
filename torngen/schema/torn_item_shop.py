import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .country_enum import CountryEnum
from .shop_name_enum import ShopNameEnum


@dataclass
class TornItemShop(BaseSchema):
    """
    JSON object of `TornItemShop`.
    """

    shop: ShopNameEnum
    sell_price: None | int
    country: CountryEnum
    buy_price: None | int

    @staticmethod
    def parse(data):
        return TornItemShop(
            shop=BaseSchema.parse(data.get("shop"), ShopNameEnum),
            sell_price=BaseSchema.parse(data.get("sell_price"), None | int),
            country=BaseSchema.parse(data.get("country"), CountryEnum),
            buy_price=BaseSchema.parse(data.get("buy_price"), None | int),
        )

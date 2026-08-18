import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .city_shop_id import CityShopId
from .torn_city_shop_item import TornCityShopItem


@dataclass
class TornCityShop(BaseSchema):
    """
    JSON object of `TornCityShop`.
    """

    name: str
    items: typing.List[TornCityShopItem]
    id: CityShopId

    @staticmethod
    def parse(data):
        return TornCityShop(
            name=BaseSchema.parse(data.get("name"), str),
            items=BaseSchema.parse(data.get("items"), typing.List[TornCityShopItem]),
            id=BaseSchema.parse(data.get("id"), CityShopId),
        )

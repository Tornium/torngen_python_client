import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_city_shop import TornCityShop


@dataclass
class TornCityShopsResponse(BaseSchema):
    """
    JSON object of `TornCityShopsResponse`.
    """

    cityshops: typing.List[TornCityShop]

    @staticmethod
    def parse(data):
        return TornCityShopsResponse(
            cityshops=BaseSchema.parse(
                data.get("cityshops"), typing.List[TornCityShop]
            ),
        )

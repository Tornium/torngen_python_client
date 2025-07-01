import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_property import BasicProperty
from .property_modification_enum import PropertyModificationEnum


@dataclass
class MarketRentalDetails(BaseSchema):
    """
    JSON object of `MarketRentalDetails`.
    """

    property: BasicProperty
    listings: typing.List[
        typing.TypedDict(
            "",
            {
                "upkeep": int,
                "rental_period": int,
                "modifications": typing.List[PropertyModificationEnum],
                "market_price": int,
                "happy": int,
                "cost_per_day": int,
                "cost": int,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return MarketRentalDetails(
            property=BaseSchema.parse(data.get("property"), BasicProperty),
            listings=BaseSchema.parse(
                data.get("listings"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "upkeep": int,
                            "rental_period": int,
                            "modifications": typing.List[PropertyModificationEnum],
                            "market_price": int,
                            "happy": int,
                            "cost_per_day": int,
                            "cost": int,
                        },
                    )
                ],
            ),
        )

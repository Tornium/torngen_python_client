import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_property import BasicProperty
from .property_modification_enum import PropertyModificationEnum


@dataclass
class MarketPropertyDetails(BaseSchema):
    """
    JSON object of `MarketPropertyDetails`.
    """

    property: BasicProperty
    listings: typing.List[
        typing.TypedDict(
            "",
            {
                "upkeep": int,
                "modifications": typing.List[PropertyModificationEnum],
                "market_price": int,
                "happy": int,
                "cost": int,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return MarketPropertyDetails(
            property=BaseSchema.parse(data.get("property"), BasicProperty),
            listings=BaseSchema.parse(
                data.get("listings"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "upkeep": int,
                            "modifications": typing.List[PropertyModificationEnum],
                            "market_price": int,
                            "happy": int,
                            "cost": int,
                        },
                    )
                ],
            ),
        )

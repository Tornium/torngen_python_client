import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .country_enum import CountryEnum
from .item_id import ItemId


@dataclass
class ReportStockAnalysis(BaseSchema):
    """
    JSON object of `ReportStockAnalysis`.
    """

    items: typing.List[
        typing.TypedDict(
            "",
            {
                "trip_duration": int,
                "item": typing.TypedDict(
                    "",
                    {
                        "value": int,
                        "price": int,
                        "name": str,
                        "id": ItemId,
                        "due": None | int,
                    },
                ),
                "hourly_profit": int,
                "country": CountryEnum,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return ReportStockAnalysis(
            items=BaseSchema.parse(
                data.get("items"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "trip_duration": int,
                            "item": typing.TypedDict(
                                "",
                                {
                                    "value": int,
                                    "price": int,
                                    "name": str,
                                    "id": ItemId,
                                    "due": None | int,
                                },
                            ),
                            "hourly_profit": int,
                            "country": CountryEnum,
                        },
                    )
                ],
            ),
        )

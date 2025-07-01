import typing

from CountryEnum import CountryEnum
from ItemId import ItemId

from ..base_schema import BaseSchema


class ReportStockAnalysis(BaseSchema):

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

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsTrading(BaseSchema):
    """
    JSON object of `PersonalStatsTrading`.
    """

    trading: typing.TypedDict(
        "",
        {
            "trades": int,
            "points": typing.TypedDict("", {"sold": int, "bought": int}),
            "items": typing.TypedDict(
                "",
                {
                    "sent": int,
                    "bought": typing.TypedDict("", {"shops": int, "market": int}),
                    "auctions": typing.TypedDict("", {"won": int, "sold": int}),
                },
            ),
            "item_market": typing.TypedDict(
                "", {"sales": int, "revenue": int, "fees": int, "customers": int}
            ),
            "bazaar": typing.TypedDict(
                "", {"sales": int, "profit": int, "customers": int}
            ),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsTrading(
            trading=BaseSchema.parse(
                data.get("trading"),
                typing.TypedDict(
                    "",
                    {
                        "trades": int,
                        "points": typing.TypedDict("", {"sold": int, "bought": int}),
                        "items": typing.TypedDict(
                            "",
                            {
                                "sent": int,
                                "bought": typing.TypedDict(
                                    "", {"shops": int, "market": int}
                                ),
                                "auctions": typing.TypedDict(
                                    "", {"won": int, "sold": int}
                                ),
                            },
                        ),
                        "item_market": typing.TypedDict(
                            "",
                            {
                                "sales": int,
                                "revenue": int,
                                "fees": int,
                                "customers": int,
                            },
                        ),
                        "bazaar": typing.TypedDict(
                            "", {"sales": int, "profit": int, "customers": int}
                        ),
                    },
                ),
            ),
        )

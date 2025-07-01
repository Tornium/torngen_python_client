import typing

from ..base_schema import BaseSchema


class PersonalStatsTrading(BaseSchema):

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

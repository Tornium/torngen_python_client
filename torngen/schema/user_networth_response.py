import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserNetworthResponse(BaseSchema):
    """
    JSON object of `UserNetworthResponse`.
    """

    networth: typing.TypedDict(
        "",
        {
            "total": int,
            "timestamp": int,
            "points": int,
            "money": typing.TypedDict(
                "",
                {
                    "wallet": int,
                    "vault": int,
                    "unpaid_fees": int,
                    "piggy_bank": int,
                    "pending": int,
                    "loans": int,
                    "city_bank": int,
                    "cayman_bank": int,
                    "bookie": int,
                },
            ),
            "items": typing.TypedDict(
                "",
                {
                    "trades": int,
                    "item_market": int,
                    "inventory": int,
                    "enlisted_cars": int,
                    "display_case": int,
                    "bazaar": int,
                    "auction_house": int,
                },
            ),
            "assets": typing.TypedDict(
                "", {"stock_market": int, "property": int, "company": int}
            ),
        },
    )

    @staticmethod
    def parse(data):
        return UserNetworthResponse(
            networth=BaseSchema.parse(
                data.get("networth"),
                typing.TypedDict(
                    "",
                    {
                        "total": int,
                        "timestamp": int,
                        "points": int,
                        "money": typing.TypedDict(
                            "",
                            {
                                "wallet": int,
                                "vault": int,
                                "unpaid_fees": int,
                                "piggy_bank": int,
                                "pending": int,
                                "loans": int,
                                "city_bank": int,
                                "cayman_bank": int,
                                "bookie": int,
                            },
                        ),
                        "items": typing.TypedDict(
                            "",
                            {
                                "trades": int,
                                "item_market": int,
                                "inventory": int,
                                "enlisted_cars": int,
                                "display_case": int,
                                "bazaar": int,
                                "auction_house": int,
                            },
                        ),
                        "assets": typing.TypedDict(
                            "", {"stock_market": int, "property": int, "company": int}
                        ),
                    },
                ),
            ),
        )

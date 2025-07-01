import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsNetworthExtended(BaseSchema):
    """
    JSON object of `PersonalStatsNetworthExtended`.
    """

    networth: typing.TypedDict(
        "",
        {
            "wallet": int,
            "vaults": int,
            "unpaid_fees": int,
            "total": int,
            "stock_market": int,
            "property": int,
            "points": int,
            "piggy_bank": int,
            "pending": int,
            "overseas_bank": int,
            "loans": int,
            "item_market": int,
            "inventory": int,
            "enlisted_cars": int,
            "display_case": int,
            "company": int,
            "bookie": int,
            "bazaar": int,
            "bank": int,
            "auction_house": int,
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsNetworthExtended(
            networth=BaseSchema.parse(
                data.get("networth"),
                typing.TypedDict(
                    "",
                    {
                        "wallet": int,
                        "vaults": int,
                        "unpaid_fees": int,
                        "total": int,
                        "stock_market": int,
                        "property": int,
                        "points": int,
                        "piggy_bank": int,
                        "pending": int,
                        "overseas_bank": int,
                        "loans": int,
                        "item_market": int,
                        "inventory": int,
                        "enlisted_cars": int,
                        "display_case": int,
                        "company": int,
                        "bookie": int,
                        "bazaar": int,
                        "bank": int,
                        "auction_house": int,
                    },
                ),
            ),
        )

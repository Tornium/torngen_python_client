import typing

from ..base_schema import BaseSchema


class PersonalStatsNetworthExtended(BaseSchema):

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

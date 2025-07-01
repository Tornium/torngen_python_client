import typing

from ..base_schema import BaseSchema


class PersonalStatsInvestments(BaseSchema):

    investments: typing.TypedDict(
        "",
        {
            "stocks": typing.TypedDict(
                "",
                {
                    "profits": int,
                    "payouts": int,
                    "net_profits": int,
                    "losses": int,
                    "fees": int,
                },
            ),
            "bank": typing.TypedDict(
                "", {"total": int, "time_remaining": int, "profit": int, "current": int}
            ),
        },
    )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsInvestments(BaseSchema):
    """
    JSON object of `PersonalStatsInvestments`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsInvestments(
            investments=BaseSchema.parse(
                data.get("investments"),
                typing.TypedDict(
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
                            "",
                            {
                                "total": int,
                                "time_remaining": int,
                                "profit": int,
                                "current": int,
                            },
                        ),
                    },
                ),
            ),
        )

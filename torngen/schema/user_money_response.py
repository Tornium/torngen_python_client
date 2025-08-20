import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserMoneyResponse(BaseSchema):
    """
    JSON object of `UserMoneyResponse`.
    """

    money: typing.TypedDict(
        "",
        {
            "wallet": int,
            "vault": int,
            "points": int,
            "faction": typing.TypedDict("", {"points": int, "money": int}),
            "daily_networth": int,
            "company": int,
            "city_bank": typing.TypedDict("", {"until": int, "amount": int}),
            "cayman_bank": int,
        },
    )

    @staticmethod
    def parse(data):
        return UserMoneyResponse(
            money=BaseSchema.parse(
                data.get("money"),
                typing.TypedDict(
                    "",
                    {
                        "wallet": int,
                        "vault": int,
                        "points": int,
                        "faction": typing.TypedDict("", {"points": int, "money": int}),
                        "daily_networth": int,
                        "company": int,
                        "city_bank": typing.TypedDict(
                            "", {"until": int, "amount": int}
                        ),
                        "cayman_bank": int,
                    },
                ),
            ),
        )

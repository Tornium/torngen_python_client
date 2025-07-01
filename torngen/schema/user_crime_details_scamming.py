import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsScamming(BaseSchema):
    """
    JSON object of `UserCrimeDetailsScamming`.
    """

    zones: typing.TypedDict(
        "",
        {
            "temptation": int,
            "sensitivity": int,
            "red": int,
            "neutral": int,
            "medium_reward": int,
            "low_reward": int,
            "high_reward": int,
            "hesitation": int,
            "concern": int,
        },
    )
    payouts: typing.TypedDict("", {"medium": int, "low": int, "high": int})
    most_responses: int
    emails: typing.TypedDict("", {"scraper": int, "phisher": int})
    concerns: typing.TypedDict("", {"resolved": int, "attempts": int})

    @staticmethod
    def parse(data):
        return UserCrimeDetailsScamming(
            zones=BaseSchema.parse(
                data.get("zones"),
                typing.TypedDict(
                    "",
                    {
                        "temptation": int,
                        "sensitivity": int,
                        "red": int,
                        "neutral": int,
                        "medium_reward": int,
                        "low_reward": int,
                        "high_reward": int,
                        "hesitation": int,
                        "concern": int,
                    },
                ),
            ),
            payouts=BaseSchema.parse(
                data.get("payouts"),
                typing.TypedDict("", {"medium": int, "low": int, "high": int}),
            ),
            most_responses=BaseSchema.parse(data.get("most_responses"), int),
            emails=BaseSchema.parse(
                data.get("emails"),
                typing.TypedDict("", {"scraper": int, "phisher": int}),
            ),
            concerns=BaseSchema.parse(
                data.get("concerns"),
                typing.TypedDict("", {"resolved": int, "attempts": int}),
            ),
        )

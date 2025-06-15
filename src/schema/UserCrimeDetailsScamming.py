import typing

from ..base_schema import BaseSchema


class UserCrimeDetailsScamming(BaseSchema):

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

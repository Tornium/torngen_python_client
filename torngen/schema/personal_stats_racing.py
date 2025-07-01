import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsRacing(BaseSchema):
    """
    JSON object of `PersonalStatsRacing`.
    """

    racing: typing.TypedDict(
        "",
        {
            "skill": int,
            "races": typing.TypedDict("", {"won": int, "entered": int}),
            "points": int,
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsRacing(
            racing=BaseSchema.parse(
                data.get("racing"),
                typing.TypedDict(
                    "",
                    {
                        "skill": int,
                        "races": typing.TypedDict("", {"won": int, "entered": int}),
                        "points": int,
                    },
                ),
            ),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsOtherPopular(BaseSchema):
    """
    JSON object of `PersonalStatsOtherPopular`.
    """

    other: typing.TypedDict(
        "",
        {
            "refills": typing.TypedDict("", {"nerve": int, "energy": int}),
            "ranked_war_wins": int,
            "merits_bought": int,
            "donator_days": int,
            "awards": int,
            "activity": typing.TypedDict(
                "",
                {
                    "time": int,
                    "streak": typing.TypedDict("", {"current": int, "best": int}),
                },
            ),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsOtherPopular(
            other=BaseSchema.parse(
                data.get("other"),
                typing.TypedDict(
                    "",
                    {
                        "refills": typing.TypedDict("", {"nerve": int, "energy": int}),
                        "ranked_war_wins": int,
                        "merits_bought": int,
                        "donator_days": int,
                        "awards": int,
                        "activity": typing.TypedDict(
                            "",
                            {
                                "time": int,
                                "streak": typing.TypedDict(
                                    "", {"current": int, "best": int}
                                ),
                            },
                        ),
                    },
                ),
            ),
        )

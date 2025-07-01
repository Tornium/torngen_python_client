import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsOther(BaseSchema):
    """
    JSON object of `PersonalStatsOther`.
    """

    other: typing.TypedDict(
        "",
        {
            "refills": typing.TypedDict(
                "", {"token": int, "nerve": int, "energy": int}
            ),
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
        return PersonalStatsOther(
            other=BaseSchema.parse(
                data.get("other"),
                typing.TypedDict(
                    "",
                    {
                        "refills": typing.TypedDict(
                            "", {"token": int, "nerve": int, "energy": int}
                        ),
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

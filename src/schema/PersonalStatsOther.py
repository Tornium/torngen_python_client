import typing

from ..base_schema import BaseSchema


class PersonalStatsOther(BaseSchema):

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

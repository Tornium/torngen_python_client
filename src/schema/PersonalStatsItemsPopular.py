import typing

from ..base_schema import BaseSchema


class PersonalStatsItemsPopular(BaseSchema):

    items: typing.TypedDict(
        "",
        {
            "used": typing.TypedDict(
                "",
                {
                    "stat_enhancers": int,
                    "energy_drinks": int,
                    "easter_eggs": int,
                    "consumables": int,
                    "candy": int,
                    "boosters": int,
                    "books": int,
                    "alcohol": int,
                },
            ),
            "found": typing.TypedDict("", {"dump": int}),
        },
    )

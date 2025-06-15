import typing

from ..base_schema import BaseSchema


class PersonalStatsItems(BaseSchema):

    items: typing.TypedDict(
        "",
        {
            "viruses_coded": int,
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
            "trashed": int,
            "found": typing.TypedDict(
                "", {"easter_eggs": int, "dump": int, "city": int}
            ),
        },
    )

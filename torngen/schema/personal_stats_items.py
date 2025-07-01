import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsItems(BaseSchema):
    """
    JSON object of `PersonalStatsItems`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsItems(
            items=BaseSchema.parse(
                data.get("items"),
                typing.TypedDict(
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
                ),
            ),
        )

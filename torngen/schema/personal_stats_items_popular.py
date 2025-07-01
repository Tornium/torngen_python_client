import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsItemsPopular(BaseSchema):
    """
    JSON object of `PersonalStatsItemsPopular`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsItemsPopular(
            items=BaseSchema.parse(
                data.get("items"),
                typing.TypedDict(
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
                ),
            ),
        )

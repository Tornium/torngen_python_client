import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornEducationRewards(BaseSchema):
    """
    JSON object of `TornEducationRewards`.
    """

    working_stats: typing.TypedDict(
        "",
        {
            "manual_labor": None | int,
            "intelligence": None | int,
            "endurance": None | int,
        },
    )
    honor: None | str
    effect: None | str

    @staticmethod
    def parse(data):
        return TornEducationRewards(
            working_stats=BaseSchema.parse(
                data.get("working_stats"),
                typing.TypedDict(
                    "",
                    {
                        "manual_labor": None | int,
                        "intelligence": None | int,
                        "endurance": None | int,
                    },
                ),
            ),
            honor=BaseSchema.parse(data.get("honor"), None | str),
            effect=BaseSchema.parse(data.get("effect"), None | str),
        )

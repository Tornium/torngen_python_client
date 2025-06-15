import typing

from ..base_schema import BaseSchema


class TornEducationRewards(BaseSchema):

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

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserWorkStatsResponse(BaseSchema):
    """
    JSON object of `UserWorkStatsResponse`.
    """

    workstats: typing.TypedDict(
        "", {"total": int, "manual_labor": int, "intelligence": int, "endurance": int}
    )

    @staticmethod
    def parse(data):
        return UserWorkStatsResponse(
            workstats=BaseSchema.parse(
                data.get("workstats"),
                typing.TypedDict(
                    "",
                    {
                        "total": int,
                        "manual_labor": int,
                        "intelligence": int,
                        "endurance": int,
                    },
                ),
            ),
        )

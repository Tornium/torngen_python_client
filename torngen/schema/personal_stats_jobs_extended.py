import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsJobsExtended(BaseSchema):
    """
    JSON object of `PersonalStatsJobsExtended`.
    """

    jobs: typing.TypedDict(
        "",
        {
            "trains_received": int,
            "stats": typing.TypedDict(
                "", {"total": int, "manual": int, "intelligence": int, "endurance": int}
            ),
            "job_points_used": int,
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsJobsExtended(
            jobs=BaseSchema.parse(
                data.get("jobs"),
                typing.TypedDict(
                    "",
                    {
                        "trains_received": int,
                        "stats": typing.TypedDict(
                            "",
                            {
                                "total": int,
                                "manual": int,
                                "intelligence": int,
                                "endurance": int,
                            },
                        ),
                        "job_points_used": int,
                    },
                ),
            ),
        )

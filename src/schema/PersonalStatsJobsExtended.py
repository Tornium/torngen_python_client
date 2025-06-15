import typing

from ..base_schema import BaseSchema


class PersonalStatsJobsExtended(BaseSchema):

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

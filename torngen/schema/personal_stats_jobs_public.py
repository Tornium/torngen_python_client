import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsJobsPublic(BaseSchema):
    """
    JSON object of `PersonalStatsJobsPublic`.
    """

    jobs: typing.TypedDict("", {"trains_received": int, "job_points_used": int})

    @staticmethod
    def parse(data):
        return PersonalStatsJobsPublic(
            jobs=BaseSchema.parse(
                data.get("jobs"),
                typing.TypedDict("", {"trains_received": int, "job_points_used": int}),
            ),
        )

import typing

from ..base_schema import BaseSchema


class PersonalStatsJobsPublic(BaseSchema):

    jobs: typing.TypedDict("", {"trains_received": int, "job_points_used": int})

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_job_ranks import UserJobRanks


@dataclass
class UserJobRanksResponse(BaseSchema):
    """
    JSON object of `UserJobRanksResponse`.
    """

    jobranks: UserJobRanks

    @staticmethod
    def parse(data):
        return UserJobRanksResponse(
            jobranks=BaseSchema.parse(data.get("jobranks"), UserJobRanks),
        )

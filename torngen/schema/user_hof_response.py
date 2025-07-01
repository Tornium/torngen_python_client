import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_hof_stats import UserHofStats


@dataclass
class UserHofResponse(BaseSchema):
    """
    JSON object of `UserHofResponse`.
    """

    hof: UserHofStats

    @staticmethod
    def parse(data):
        return UserHofResponse(
            hof=BaseSchema.parse(data.get("hof"), UserHofStats),
        )

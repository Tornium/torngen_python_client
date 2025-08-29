import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_honor import UserHonor


@dataclass
class UserHonorsResponse(BaseSchema):
    """
    JSON object of `UserHonorsResponse`.
    """

    honors: typing.List[UserHonor]

    @staticmethod
    def parse(data):
        return UserHonorsResponse(
            honors=BaseSchema.parse(data.get("honors"), typing.List[UserHonor]),
        )

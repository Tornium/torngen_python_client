import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_honor_detailed import UserHonorDetailed


@dataclass
class UserHonorsDetailedResponse(BaseSchema):
    """
    JSON object of `UserHonorsDetailedResponse`.
    """

    honors: typing.List[UserHonorDetailed]

    @staticmethod
    def parse(data):
        return UserHonorsDetailedResponse(
            honors=BaseSchema.parse(data.get("honors"), typing.List[UserHonorDetailed]),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_crime import UserCrime


@dataclass
class UserCrimesResponse(BaseSchema):
    """
    JSON object of `UserCrimesResponse`.
    """

    crimes: UserCrime

    @staticmethod
    def parse(data):
        return UserCrimesResponse(
            crimes=BaseSchema.parse(data.get("crimes"), UserCrime),
        )

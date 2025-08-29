import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_medal import UserMedal


@dataclass
class UserMedalsResponse(BaseSchema):
    """
    JSON object of `UserMedalsResponse`.
    """

    medals: typing.List[UserMedal]

    @staticmethod
    def parse(data):
        return UserMedalsResponse(
            medals=BaseSchema.parse(data.get("medals"), typing.List[UserMedal]),
        )

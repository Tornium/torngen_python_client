import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_medal_detailed import UserMedalDetailed


@dataclass
class UserMedalsDetailedResponse(BaseSchema):
    """
    JSON object of `UserMedalsDetailedResponse`.
    """

    medals: typing.List[UserMedalDetailed]

    @staticmethod
    def parse(data):
        return UserMedalsDetailedResponse(
            medals=BaseSchema.parse(data.get("medals"), typing.List[UserMedalDetailed]),
        )

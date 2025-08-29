import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_merit_upgrade import UserMeritUpgrade


@dataclass
class UserMerits(BaseSchema):
    """
    JSON object of `UserMerits`.
    """

    used: int
    upgrades: typing.List[UserMeritUpgrade]
    medals: int
    honors: int
    available: int

    @staticmethod
    def parse(data):
        return UserMerits(
            used=BaseSchema.parse(data.get("used"), int),
            upgrades=BaseSchema.parse(
                data.get("upgrades"), typing.List[UserMeritUpgrade]
            ),
            medals=BaseSchema.parse(data.get("medals"), int),
            honors=BaseSchema.parse(data.get("honors"), int),
            available=BaseSchema.parse(data.get("available"), int),
        )

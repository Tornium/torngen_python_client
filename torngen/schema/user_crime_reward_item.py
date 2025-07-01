import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeRewardItem(BaseSchema):
    """
    JSON object of `UserCrimeRewardItem`.
    """

    id: int
    amount: int

    @staticmethod
    def parse(data):
        return UserCrimeRewardItem(
            id=BaseSchema.parse(data.get("id"), int),
            amount=BaseSchema.parse(data.get("amount"), int),
        )

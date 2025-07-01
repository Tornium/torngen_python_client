import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_subcrime import UserSubcrime


@dataclass
class UserCrimeAttempts(BaseSchema):
    """
    JSON object of `UserCrimeAttempts`.
    """

    total: int
    success: int
    subcrimes: typing.List[UserSubcrime]
    fail: int
    critical_fail: int

    @staticmethod
    def parse(data):
        return UserCrimeAttempts(
            total=BaseSchema.parse(data.get("total"), int),
            success=BaseSchema.parse(data.get("success"), int),
            subcrimes=BaseSchema.parse(
                data.get("subcrimes"), typing.List[UserSubcrime]
            ),
            fail=BaseSchema.parse(data.get("fail"), int),
            critical_fail=BaseSchema.parse(data.get("critical_fail"), int),
        )

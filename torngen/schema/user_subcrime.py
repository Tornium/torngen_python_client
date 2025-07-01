import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserSubcrime(BaseSchema):
    """
    JSON object of `UserSubcrime`.
    """

    total: int
    success: int
    id: int
    fail: int

    @staticmethod
    def parse(data):
        return UserSubcrime(
            total=BaseSchema.parse(data.get("total"), int),
            success=BaseSchema.parse(data.get("success"), int),
            id=BaseSchema.parse(data.get("id"), int),
            fail=BaseSchema.parse(data.get("fail"), int),
        )

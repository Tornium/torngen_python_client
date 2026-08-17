import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_sub_crime_id import TornSubCrimeId


@dataclass
class UserSubcrime(BaseSchema):
    """
    JSON object of `UserSubcrime`.
    """

    total: int
    success: int
    id: TornSubCrimeId
    fail: int

    @staticmethod
    def parse(data):
        return UserSubcrime(
            total=BaseSchema.parse(data.get("total"), int),
            success=BaseSchema.parse(data.get("success"), int),
            id=BaseSchema.parse(data.get("id"), TornSubCrimeId),
            fail=BaseSchema.parse(data.get("fail"), int),
        )

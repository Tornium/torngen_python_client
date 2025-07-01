import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsShoplifting(BaseSchema):
    """
    JSON object of `UserCrimeDetailsShoplifting`.
    """

    average_notoriety: int

    @staticmethod
    def parse(data):
        return UserCrimeDetailsShoplifting(
            average_notoriety=BaseSchema.parse(data.get("average_notoriety"), int),
        )

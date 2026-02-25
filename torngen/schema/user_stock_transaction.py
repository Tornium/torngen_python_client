import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserStockTransaction(BaseSchema):
    """
    JSON object of `UserStockTransaction`.
    """

    timestamp: int
    shares: int
    price: int
    id: int

    @staticmethod
    def parse(data):
        return UserStockTransaction(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            shares=BaseSchema.parse(data.get("shares"), int),
            price=BaseSchema.parse(data.get("price"), int),
            id=BaseSchema.parse(data.get("id"), int),
        )

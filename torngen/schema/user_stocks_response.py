import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_stock import UserStock


@dataclass
class UserStocksResponse(BaseSchema):
    """
    JSON object of `UserStocksResponse`.
    """

    stocks: typing.List[UserStock]

    @staticmethod
    def parse(data):
        return UserStocksResponse(
            stocks=BaseSchema.parse(data.get("stocks"), typing.List[UserStock]),
        )

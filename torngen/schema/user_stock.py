import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .stock_id import StockId
from .user_stock_transaction import UserStockTransaction


@dataclass
class UserStock(BaseSchema):
    """
    JSON object of `UserStock`.
    """

    transactions: typing.List[UserStockTransaction]
    shares: int
    id: StockId
    bonus: typing.TypedDict(
        "", {"progress": int, "increment": int, "frequency": int, "available": bool}
    )

    @staticmethod
    def parse(data):
        return UserStock(
            transactions=BaseSchema.parse(
                data.get("transactions"), typing.List[UserStockTransaction]
            ),
            shares=BaseSchema.parse(data.get("shares"), int),
            id=BaseSchema.parse(data.get("id"), StockId),
            bonus=BaseSchema.parse(
                data.get("bonus"),
                typing.TypedDict(
                    "",
                    {
                        "progress": int,
                        "increment": int,
                        "frequency": int,
                        "available": bool,
                    },
                ),
            ),
        )

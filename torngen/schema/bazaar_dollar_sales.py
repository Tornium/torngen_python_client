import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class BazaarDollarSales(BaseSchema):

    dollar_sales: int
    name: str
    is_open: bool
    id: UserId

    @staticmethod
    def parse(data):
        return BazaarDollarSales(
            dollar_sales=BaseSchema.parse(data.get("dollar_sales"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_open=BaseSchema.parse(data.get("is_open"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

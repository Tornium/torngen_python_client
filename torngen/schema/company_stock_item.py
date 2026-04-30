import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyStockItem(BaseSchema):
    """
    JSON object of `CompanyStockItem`.
    """

    sold_worth: int
    sold_amount: int
    rrp: int
    price: int
    on_order: int
    name: str
    in_stock: int
    id: int
    cost: int

    @staticmethod
    def parse(data):
        return CompanyStockItem(
            sold_worth=BaseSchema.parse(data.get("sold_worth"), int),
            sold_amount=BaseSchema.parse(data.get("sold_amount"), int),
            rrp=BaseSchema.parse(data.get("rrp"), int),
            price=BaseSchema.parse(data.get("price"), int),
            on_order=BaseSchema.parse(data.get("on_order"), int),
            name=BaseSchema.parse(data.get("name"), str),
            in_stock=BaseSchema.parse(data.get("in_stock"), int),
            id=BaseSchema.parse(data.get("id"), int),
            cost=BaseSchema.parse(data.get("cost"), int),
        )

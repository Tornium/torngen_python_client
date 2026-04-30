import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_stock_item import CompanyStockItem


@dataclass
class CompanyStockResponse(BaseSchema):
    """
    JSON object of `CompanyStockResponse`.
    """

    stock: typing.List[CompanyStockItem]

    @staticmethod
    def parse(data):
        return CompanyStockResponse(
            stock=BaseSchema.parse(data.get("stock"), typing.List[CompanyStockItem]),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_stock_id import CompanyStockId


@dataclass
class TornCompanyStock(BaseSchema):
    """
    JSON object of `TornCompanyStock`.
    """

    rrp: int
    name: str
    id: CompanyStockId
    cost: int

    @staticmethod
    def parse(data):
        return TornCompanyStock(
            rrp=BaseSchema.parse(data.get("rrp"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyStockId),
            cost=BaseSchema.parse(data.get("cost"), int),
        )

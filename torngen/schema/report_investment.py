import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ReportInvestment(BaseSchema):
    """
    JSON object of `ReportInvestment`.
    """

    until: int
    amount: int

    @staticmethod
    def parse(data):
        return ReportInvestment(
            until=BaseSchema.parse(data.get("until"), int),
            amount=BaseSchema.parse(data.get("amount"), int),
        )

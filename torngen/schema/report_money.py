import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ReportMoney(BaseSchema):
    """
    JSON object of `ReportMoney`.
    """

    money: int

    @staticmethod
    def parse(data):
        return ReportMoney(
            money=BaseSchema.parse(data.get("money"), int),
        )

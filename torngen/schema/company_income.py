import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyIncome(BaseSchema):
    """
    JSON object of `CompanyIncome`.
    """

    weekly: int
    daily: int

    @staticmethod
    def parse(data):
        return CompanyIncome(
            weekly=BaseSchema.parse(data.get("weekly"), int),
            daily=BaseSchema.parse(data.get("daily"), int),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyCustomers(BaseSchema):
    """
    JSON object of `CompanyCustomers`.
    """

    weekly: int
    daily: int

    @staticmethod
    def parse(data):
        return CompanyCustomers(
            weekly=BaseSchema.parse(data.get("weekly"), int),
            daily=BaseSchema.parse(data.get("daily"), int),
        )

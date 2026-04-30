import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyEmployees(BaseSchema):
    """
    JSON object of `CompanyEmployees`.
    """

    hired: int
    capacity: int

    @staticmethod
    def parse(data):
        return CompanyEmployees(
            hired=BaseSchema.parse(data.get("hired"), int),
            capacity=BaseSchema.parse(data.get("capacity"), int),
        )

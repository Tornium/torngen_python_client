import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyEmployeeStats(BaseSchema):
    """
    JSON object of `CompanyEmployeeStats`.
    """

    manual_labor: int
    intelligence: int
    endurance: int

    @staticmethod
    def parse(data):
        return CompanyEmployeeStats(
            manual_labor=BaseSchema.parse(data.get("manual_labor"), int),
            intelligence=BaseSchema.parse(data.get("intelligence"), int),
            endurance=BaseSchema.parse(data.get("endurance"), int),
        )

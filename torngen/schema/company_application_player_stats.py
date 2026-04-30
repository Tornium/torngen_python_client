import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class CompanyApplicationPlayerStats(BaseSchema):
    """
    JSON object of `CompanyApplicationPlayerStats`.
    """

    manual_labor: int
    intelligence: int
    endurance: int

    @staticmethod
    def parse(data):
        return CompanyApplicationPlayerStats(
            manual_labor=BaseSchema.parse(data.get("manual_labor"), int),
            intelligence=BaseSchema.parse(data.get("intelligence"), int),
            endurance=BaseSchema.parse(data.get("endurance"), int),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_company import TornCompany


@dataclass
class TornCompaniesResponse(BaseSchema):
    """
    JSON object of `TornCompaniesResponse`.
    """

    companies: typing.List[TornCompany]

    @staticmethod
    def parse(data):
        return TornCompaniesResponse(
            companies=BaseSchema.parse(data.get("companies"), typing.List[TornCompany]),
        )

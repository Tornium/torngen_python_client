import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_position_id import CompanyPositionId


@dataclass
class CompanyEmployeePosition(BaseSchema):
    """
    JSON object of `CompanyEmployeePosition`.
    """

    name: str
    id: CompanyPositionId

    @staticmethod
    def parse(data):
        return CompanyEmployeePosition(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyPositionId),
        )

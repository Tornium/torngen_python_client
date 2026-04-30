import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_type_id import CompanyTypeId


@dataclass
class CompanyType(BaseSchema):
    """
    JSON object of `CompanyType`.
    """

    name: str
    id: CompanyTypeId

    @staticmethod
    def parse(data):
        return CompanyType(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyTypeId),
        )

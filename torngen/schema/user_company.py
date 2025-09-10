import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_id import CompanyId
from .company_type_id import CompanyTypeId


@dataclass
class UserCompany(BaseSchema):
    """
    JSON object of `UserCompany`.
    """

    type_id: CompanyTypeId
    type: typing.Literal["company"]
    rating: int
    position: str
    name: str
    id: CompanyId
    days_in_company: int

    @staticmethod
    def parse(data):
        return UserCompany(
            type_id=BaseSchema.parse(data.get("type_id"), CompanyTypeId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["company"]),
            rating=BaseSchema.parse(data.get("rating"), int),
            position=BaseSchema.parse(data.get("position"), str),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), CompanyId),
            days_in_company=BaseSchema.parse(data.get("days_in_company"), int),
        )

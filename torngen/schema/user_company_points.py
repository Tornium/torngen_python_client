import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_type_id import CompanyTypeId


@dataclass
class UserCompanyPoints(BaseSchema):
    """
    JSON object of `UserCompanyPoints`.
    """

    points: int
    company: typing.TypedDict("", {"name": str, "id": CompanyTypeId})

    @staticmethod
    def parse(data):
        return UserCompanyPoints(
            points=BaseSchema.parse(data.get("points"), int),
            company=BaseSchema.parse(
                data.get("company"),
                typing.TypedDict("", {"name": str, "id": CompanyTypeId}),
            ),
        )

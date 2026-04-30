import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_application import CompanyApplication


@dataclass
class CompanyApplicationsResponse(BaseSchema):
    """
    JSON object of `CompanyApplicationsResponse`.
    """

    applications: typing.List[CompanyApplication]

    @staticmethod
    def parse(data):
        return CompanyApplicationsResponse(
            applications=BaseSchema.parse(
                data.get("applications"), typing.List[CompanyApplication]
            ),
        )

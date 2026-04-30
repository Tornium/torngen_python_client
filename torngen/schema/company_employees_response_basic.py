import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_employee import CompanyEmployee


@dataclass
class CompanyEmployeesResponseBasic(BaseSchema):
    """
    JSON object of `CompanyEmployeesResponseBasic`.
    """

    employees: typing.List[CompanyEmployee]

    @staticmethod
    def parse(data):
        return CompanyEmployeesResponseBasic(
            employees=BaseSchema.parse(
                data.get("employees"), typing.List[CompanyEmployee]
            ),
        )

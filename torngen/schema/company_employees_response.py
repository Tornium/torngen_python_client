import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_employee import CompanyEmployee
from .company_employee_extended import CompanyEmployeeExtended


@dataclass
class CompanyEmployeesResponse(BaseSchema):
    """
    JSON object of `CompanyEmployeesResponse`.
    """

    employees: typing.List[CompanyEmployeeExtended | CompanyEmployee]

    @staticmethod
    def parse(data):
        return CompanyEmployeesResponse(
            employees=BaseSchema.parse(
                data.get("employees"),
                typing.List[CompanyEmployeeExtended | CompanyEmployee],
            ),
        )

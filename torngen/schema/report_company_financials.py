import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ReportCompanyFinancials(BaseSchema):
    """
    JSON object of `ReportCompanyFinancials`.
    """

    wages: typing.TypedDict("", {"lowest": int, "highest": int, "average": int})
    employees: int
    balance: int

    @staticmethod
    def parse(data):
        return ReportCompanyFinancials(
            wages=BaseSchema.parse(
                data.get("wages"),
                typing.TypedDict("", {"lowest": int, "highest": int, "average": int}),
            ),
            employees=BaseSchema.parse(data.get("employees"), int),
            balance=BaseSchema.parse(data.get("balance"), int),
        )

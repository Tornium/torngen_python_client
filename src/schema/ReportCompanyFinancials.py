import typing

from ..base_schema import BaseSchema


class ReportCompanyFinancials(BaseSchema):

    wages: typing.TypedDict("", {"lowest": int, "highest": int, "average": int})
    employees: int
    balance: int

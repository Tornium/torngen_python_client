import typing

from ..base_schema import BaseSchema


class ReportInvestment(BaseSchema):

    until: int
    amount: int

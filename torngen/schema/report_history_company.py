import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_id import CompanyId


@dataclass
class ReportHistoryCompany(BaseSchema):
    """
    JSON object of `ReportHistoryCompany`.
    """

    name: str
    left: None | str
    joined: str
    id: CompanyId

    @staticmethod
    def parse(data):
        return ReportHistoryCompany(
            name=BaseSchema.parse(data.get("name"), str),
            left=BaseSchema.parse(data.get("left"), None | str),
            joined=BaseSchema.parse(data.get("joined"), str),
            id=BaseSchema.parse(data.get("id"), CompanyId),
        )

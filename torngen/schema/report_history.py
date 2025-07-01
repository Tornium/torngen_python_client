import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .report_history_company import ReportHistoryCompany
from .report_history_faction import ReportHistoryFaction


@dataclass
class ReportHistory(BaseSchema):
    """
    JSON object of `ReportHistory`.
    """

    factions: typing.List[ReportHistoryFaction]
    companies: typing.List[ReportHistoryCompany]

    @staticmethod
    def parse(data):
        return ReportHistory(
            factions=BaseSchema.parse(
                data.get("factions"), typing.List[ReportHistoryFaction]
            ),
            companies=BaseSchema.parse(
                data.get("companies"), typing.List[ReportHistoryCompany]
            ),
        )

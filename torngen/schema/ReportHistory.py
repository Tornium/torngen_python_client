import typing

from ReportHistoryCompany import ReportHistoryCompany
from ReportHistoryFaction import ReportHistoryFaction

from ..base_schema import BaseSchema


class ReportHistory(BaseSchema):

    factions: typing.List[ReportHistoryFaction]
    companies: typing.List[ReportHistoryCompany]

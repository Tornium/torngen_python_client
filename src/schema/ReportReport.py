import typing

from ReportAnonymousBounties import ReportAnonymousBounties
from ReportCompanyFinancials import ReportCompanyFinancials
from ReportFriendOrFoe import ReportFriendOrFoe
from ReportHistory import ReportHistory
from ReportInvestment import ReportInvestment
from ReportMoney import ReportMoney
from ReportMostWanted import ReportMostWanted
from ReportStats import ReportStats
from ReportStockAnalysis import ReportStockAnalysis
from ReportTrueLevel import ReportTrueLevel

from ..base_schema import BaseSchema


class ReportReport(BaseSchema):

    report: (
        ReportInvestment
        | ReportAnonymousBounties
        | ReportStockAnalysis
        | ReportTrueLevel
        | ReportCompanyFinancials
        | ReportFriendOrFoe
        | ReportHistory
        | ReportMostWanted
        | ReportStats
        | ReportMoney
    )

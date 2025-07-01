import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .report_anonymous_bounties import ReportAnonymousBounties
from .report_company_financials import ReportCompanyFinancials
from .report_friend_or_foe import ReportFriendOrFoe
from .report_history import ReportHistory
from .report_investment import ReportInvestment
from .report_money import ReportMoney
from .report_most_wanted import ReportMostWanted
from .report_stats import ReportStats
from .report_stock_analysis import ReportStockAnalysis
from .report_true_level import ReportTrueLevel


@dataclass
class ReportReport(BaseSchema):
    """
    JSON object of `ReportReport`.
    """

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

    @staticmethod
    def parse(data):
        return ReportReport(
            report=BaseSchema.parse(
                data.get("report"),
                ReportInvestment
                | ReportAnonymousBounties
                | ReportStockAnalysis
                | ReportTrueLevel
                | ReportCompanyFinancials
                | ReportFriendOrFoe
                | ReportHistory
                | ReportMostWanted
                | ReportStats
                | ReportMoney,
            ),
        )

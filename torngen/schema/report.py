import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
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
from .report_type_enum import ReportTypeEnum
from .user_id import UserId


@dataclass
class Report(BaseSchema):

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
    type: ReportTypeEnum
    timestamp: int
    target_id: None | UserId
    reporter_id: UserId
    faction_id: None | FactionId

    @staticmethod
    def parse(data):
        return Report(
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
            type=BaseSchema.parse(data.get("type"), ReportTypeEnum),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            target_id=BaseSchema.parse(data.get("target_id"), None | UserId),
            reporter_id=BaseSchema.parse(data.get("reporter_id"), UserId),
            faction_id=BaseSchema.parse(data.get("faction_id"), None | FactionId),
        )

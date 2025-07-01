import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .chain_id import ChainId
from .faction_chain_report_attacker import FactionChainReportAttacker
from .faction_chain_report_bonus import FactionChainReportBonus
from .faction_chain_report_details import FactionChainReportDetails
from .faction_id import FactionId
from .user_id import UserId


@dataclass
class FactionChainReport(BaseSchema):
    """
    JSON object of `FactionChainReport`.
    """

    start: int
    non_attackers: typing.List[UserId]
    id: ChainId
    faction_id: FactionId
    end: int
    details: FactionChainReportDetails
    bonuses: typing.List[FactionChainReportBonus]
    attackers: typing.List[FactionChainReportAttacker]

    @staticmethod
    def parse(data):
        return FactionChainReport(
            start=BaseSchema.parse(data.get("start"), int),
            non_attackers=BaseSchema.parse(
                data.get("non_attackers"), typing.List[UserId]
            ),
            id=BaseSchema.parse(data.get("id"), ChainId),
            faction_id=BaseSchema.parse(data.get("faction_id"), FactionId),
            end=BaseSchema.parse(data.get("end"), int),
            details=BaseSchema.parse(data.get("details"), FactionChainReportDetails),
            bonuses=BaseSchema.parse(
                data.get("bonuses"), typing.List[FactionChainReportBonus]
            ),
            attackers=BaseSchema.parse(
                data.get("attackers"), typing.List[FactionChainReportAttacker]
            ),
        )

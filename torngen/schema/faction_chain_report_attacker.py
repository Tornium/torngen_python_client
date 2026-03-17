import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_chain_report_attacker_attacks import \
    FactionChainReportAttackerAttacks
from .faction_chain_report_attacker_respect import \
    FactionChainReportAttackerRespect
from .user_id import UserId


@dataclass
class FactionChainReportAttacker(BaseSchema):
    """
    JSON object of `FactionChainReportAttacker`.
    """

    respect: FactionChainReportAttackerRespect
    id: UserId
    attacks: FactionChainReportAttackerAttacks

    @staticmethod
    def parse(data):
        return FactionChainReportAttacker(
            respect=BaseSchema.parse(
                data.get("respect"), FactionChainReportAttackerRespect
            ),
            id=BaseSchema.parse(data.get("id"), UserId),
            attacks=BaseSchema.parse(
                data.get("attacks"), FactionChainReportAttackerAttacks
            ),
        )

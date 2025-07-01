import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionChainReportBonus(BaseSchema):
    """
    JSON object of `FactionChainReportBonus`.
    """

    respect: int
    defender_id: UserId
    chain: int
    attacker_id: UserId

    @staticmethod
    def parse(data):
        return FactionChainReportBonus(
            respect=BaseSchema.parse(data.get("respect"), int),
            defender_id=BaseSchema.parse(data.get("defender_id"), UserId),
            chain=BaseSchema.parse(data.get("chain"), int),
            attacker_id=BaseSchema.parse(data.get("attacker_id"), UserId),
        )

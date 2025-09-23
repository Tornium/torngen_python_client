import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionChainReportAttackerAttacks(BaseSchema):
    """
    JSON object of `FactionChainReportAttackerAttacks`.
    """

    war: int
    total: int
    retaliations: int
    overseas: int
    mug: int
    losses: int
    leave: int
    hospitalize: int
    escapes: typing.Optional[int]
    draws: int
    bonuses: int
    assists: int

    @staticmethod
    def parse(data):
        return FactionChainReportAttackerAttacks(
            war=BaseSchema.parse(data.get("war"), int),
            total=BaseSchema.parse(data.get("total"), int),
            retaliations=BaseSchema.parse(data.get("retaliations"), int),
            overseas=BaseSchema.parse(data.get("overseas"), int),
            mug=BaseSchema.parse(data.get("mug"), int),
            losses=BaseSchema.parse(data.get("losses"), int),
            leave=BaseSchema.parse(data.get("leave"), int),
            hospitalize=BaseSchema.parse(data.get("hospitalize"), int),
            escapes=BaseSchema.parse(data.get("escapes"), typing.Optional[int]),
            draws=BaseSchema.parse(data.get("draws"), int),
            bonuses=BaseSchema.parse(data.get("bonuses"), int),
            assists=BaseSchema.parse(data.get("assists"), int),
        )

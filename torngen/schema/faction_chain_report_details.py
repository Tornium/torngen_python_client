import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionChainReportDetails(BaseSchema):
    """
    JSON object of `FactionChainReportDetails`.
    """

    war: int
    targets: int
    retaliations: int
    respect: int | float
    overseas: int
    mug: int
    members: int
    losses: int
    leave: int
    hospitalize: int
    escapes: int
    draws: int
    chain: int
    best: int | float
    assists: int

    @staticmethod
    def parse(data):
        return FactionChainReportDetails(
            war=BaseSchema.parse(data.get("war"), int),
            targets=BaseSchema.parse(data.get("targets"), int),
            retaliations=BaseSchema.parse(data.get("retaliations"), int),
            respect=BaseSchema.parse(data.get("respect"), int | float),
            overseas=BaseSchema.parse(data.get("overseas"), int),
            mug=BaseSchema.parse(data.get("mug"), int),
            members=BaseSchema.parse(data.get("members"), int),
            losses=BaseSchema.parse(data.get("losses"), int),
            leave=BaseSchema.parse(data.get("leave"), int),
            hospitalize=BaseSchema.parse(data.get("hospitalize"), int),
            escapes=BaseSchema.parse(data.get("escapes"), int),
            draws=BaseSchema.parse(data.get("draws"), int),
            chain=BaseSchema.parse(data.get("chain"), int),
            best=BaseSchema.parse(data.get("best"), int | float),
            assists=BaseSchema.parse(data.get("assists"), int),
        )

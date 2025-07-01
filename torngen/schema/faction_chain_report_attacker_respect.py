import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionChainReportAttackerRespect(BaseSchema):
    """
    JSON object of `FactionChainReportAttackerRespect`.
    """

    total: int | float
    best: int | float
    average: int | float

    @staticmethod
    def parse(data):
        return FactionChainReportAttackerRespect(
            total=BaseSchema.parse(data.get("total"), int | float),
            best=BaseSchema.parse(data.get("best"), int | float),
            average=BaseSchema.parse(data.get("average"), int | float),
        )

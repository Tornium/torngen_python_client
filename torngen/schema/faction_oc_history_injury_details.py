import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionOcHistoryInjuryDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryInjuryDetails`.
    """

    life_lost: int

    @staticmethod
    def parse(data):
        return FactionOcHistoryInjuryDetails(
            life_lost=BaseSchema.parse(data.get("life_lost"), int),
        )

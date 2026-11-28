import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_organized_crime_position_id import TornOrganizedCrimePositionId


@dataclass
class FactionOcHistoryRole(BaseSchema):
    """
    JSON object of `FactionOcHistoryRole`.
    """

    label: str
    id: None | TornOrganizedCrimePositionId

    @staticmethod
    def parse(data):
        return FactionOcHistoryRole(
            label=BaseSchema.parse(data.get("label"), str),
            id=BaseSchema.parse(data.get("id"), None | TornOrganizedCrimePositionId),
        )

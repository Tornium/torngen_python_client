import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_organized_crime_position_id import TornOrganizedCrimePositionId


@dataclass
class FactionSlotPositionInfo(BaseSchema):
    """
    JSON object of `FactionSlotPositionInfo`.
    """

    number: int
    label: str
    id: TornOrganizedCrimePositionId

    @staticmethod
    def parse(data):
        return FactionSlotPositionInfo(
            number=BaseSchema.parse(data.get("number"), int),
            label=BaseSchema.parse(data.get("label"), str),
            id=BaseSchema.parse(data.get("id"), TornOrganizedCrimePositionId),
        )

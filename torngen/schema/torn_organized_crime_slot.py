import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_organized_crime_position_id import TornOrganizedCrimePositionId
from .torn_organized_crime_required_item import TornOrganizedCrimeRequiredItem


@dataclass
class TornOrganizedCrimeSlot(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeSlot`.
    """

    required_item: None | TornOrganizedCrimeRequiredItem
    name: str
    id: TornOrganizedCrimePositionId

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeSlot(
            required_item=BaseSchema.parse(
                data.get("required_item"), None | TornOrganizedCrimeRequiredItem
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), TornOrganizedCrimePositionId),
        )

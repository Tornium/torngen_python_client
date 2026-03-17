import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_slot_position_info import FactionSlotPositionInfo
from .torn_organized_crime_position_id_deprecated import \
    TornOrganizedCrimePositionIdDeprecated
from .torn_organized_crime_required_item import TornOrganizedCrimeRequiredItem


@dataclass
class TornOrganizedCrimeSlot(BaseSchema):
    """
    JSON object of `TornOrganizedCrimeSlot`.
    """

    required_item: None | TornOrganizedCrimeRequiredItem
    position_info: FactionSlotPositionInfo
    name: str
    id: typing.Optional[TornOrganizedCrimePositionIdDeprecated]

    @staticmethod
    def parse(data):
        return TornOrganizedCrimeSlot(
            required_item=BaseSchema.parse(
                data.get("required_item"), None | TornOrganizedCrimeRequiredItem
            ),
            position_info=BaseSchema.parse(
                data.get("position_info"), FactionSlotPositionInfo
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(
                data.get("id"), typing.Optional[TornOrganizedCrimePositionIdDeprecated]
            ),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_user import FactionCrimeUser
from .faction_slot_position_info import FactionSlotPositionInfo
from .item_id import ItemId
from .torn_organized_crime_position_id_deprecated import (
    TornOrganizedCrimePositionIdDeprecated,
)


@dataclass
class FactionCrimeSlot(BaseSchema):
    """
    JSON object of `FactionCrimeSlot`.
    """

    user: None | FactionCrimeUser
    position_number: typing.Optional[int]
    position_info: FactionSlotPositionInfo
    position_id: typing.Optional[TornOrganizedCrimePositionIdDeprecated]
    position: str
    item_requirement: None | typing.TypedDict(
        "", {"is_reusable": bool, "is_available": bool, "id": ItemId}
    )
    checkpoint_pass_rate: int

    @staticmethod
    def parse(data):
        return FactionCrimeSlot(
            user=BaseSchema.parse(data.get("user"), None | FactionCrimeUser),
            position_number=BaseSchema.parse(
                data.get("position_number"), typing.Optional[int]
            ),
            position_info=BaseSchema.parse(
                data.get("position_info"), FactionSlotPositionInfo
            ),
            position_id=BaseSchema.parse(
                data.get("position_id"),
                typing.Optional[TornOrganizedCrimePositionIdDeprecated],
            ),
            position=BaseSchema.parse(data.get("position"), str),
            item_requirement=BaseSchema.parse(
                data.get("item_requirement"),
                None
                | typing.TypedDict(
                    "", {"is_reusable": bool, "is_available": bool, "id": ItemId}
                ),
            ),
            checkpoint_pass_rate=BaseSchema.parse(
                data.get("checkpoint_pass_rate"), int
            ),
        )

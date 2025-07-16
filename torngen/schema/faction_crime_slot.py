import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_user import FactionCrimeUser
from .item_id import ItemId
from .torn_organized_crime_position_id import TornOrganizedCrimePositionId


@dataclass
class FactionCrimeSlot(BaseSchema):
    """
    JSON object of `FactionCrimeSlot`.
    """

    user: None | FactionCrimeUser
    position_number: int
    position_id: TornOrganizedCrimePositionId
    position: str
    item_requirement: None | typing.TypedDict(
        "", {"is_reusable": bool, "is_available": bool, "id": ItemId}
    )
    checkpoint_pass_rate: int

    @staticmethod
    def parse(data):
        return FactionCrimeSlot(
            user=BaseSchema.parse(data.get("user"), None | FactionCrimeUser),
            position_number=BaseSchema.parse(data.get("position_number"), int),
            position_id=BaseSchema.parse(
                data.get("position_id"), TornOrganizedCrimePositionId
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

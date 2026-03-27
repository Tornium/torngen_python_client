import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_item_outcome_enum import FactionCrimeItemOutcomeEnum
from .faction_crime_user_item_outcome_enum import FactionCrimeUserItemOutcomeEnum
from .item_id import ItemId
from .item_uid import ItemUid


@dataclass
class FactionCrimeUserItemOutcome(BaseSchema):
    """
    JSON object of `FactionCrimeUserItemOutcome`.
    """

    owned_by: FactionCrimeUserItemOutcomeEnum
    outcome: FactionCrimeItemOutcomeEnum
    item_uid: ItemUid
    item_id: ItemId

    @staticmethod
    def parse(data):
        return FactionCrimeUserItemOutcome(
            owned_by=BaseSchema.parse(
                data.get("owned_by"), FactionCrimeUserItemOutcomeEnum
            ),
            outcome=BaseSchema.parse(data.get("outcome"), FactionCrimeItemOutcomeEnum),
            item_uid=BaseSchema.parse(data.get("item_uid"), ItemUid),
            item_id=BaseSchema.parse(data.get("item_id"), ItemId),
        )

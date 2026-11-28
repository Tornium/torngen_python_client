import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_id import FactionCrimeId
from .faction_oc_history_item import FactionOcHistoryItem
from .faction_oc_history_payout_destination_enum import (
    FactionOcHistoryPayoutDestinationEnum,
)
from .faction_oc_history_payout_type_enum import FactionOcHistoryPayoutTypeEnum
from .faction_oc_history_role import FactionOcHistoryRole


@dataclass
class FactionOcHistoryPayoutReceivedDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryPayoutReceivedDetails`.
    """

    type: FactionOcHistoryPayoutTypeEnum
    role: FactionOcHistoryRole
    percentage: int | float
    money: None | int
    items: typing.List[FactionOcHistoryItem]
    destination: None | FactionOcHistoryPayoutDestinationEnum
    crime_id: None | FactionCrimeId

    @staticmethod
    def parse(data):
        return FactionOcHistoryPayoutReceivedDetails(
            type=BaseSchema.parse(data.get("type"), FactionOcHistoryPayoutTypeEnum),
            role=BaseSchema.parse(data.get("role"), FactionOcHistoryRole),
            percentage=BaseSchema.parse(data.get("percentage"), int | float),
            money=BaseSchema.parse(data.get("money"), None | int),
            items=BaseSchema.parse(
                data.get("items"), typing.List[FactionOcHistoryItem]
            ),
            destination=BaseSchema.parse(
                data.get("destination"), None | FactionOcHistoryPayoutDestinationEnum
            ),
            crime_id=BaseSchema.parse(data.get("crime_id"), None | FactionCrimeId),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_oc_history_item import FactionOcHistoryItem
from .faction_oc_history_payout_destination_enum import (
    FactionOcHistoryPayoutDestinationEnum,
)
from .faction_oc_history_payout_type_enum import FactionOcHistoryPayoutTypeEnum
from .user_id import UserId


@dataclass
class FactionOcHistoryPayoutDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryPayoutDetails`.
    """

    type: FactionOcHistoryPayoutTypeEnum
    percentage: int | float
    participants: typing.List[UserId]
    money: None | int
    items: typing.List[FactionOcHistoryItem]
    destination: None | FactionOcHistoryPayoutDestinationEnum

    @staticmethod
    def parse(data):
        return FactionOcHistoryPayoutDetails(
            type=BaseSchema.parse(data.get("type"), FactionOcHistoryPayoutTypeEnum),
            percentage=BaseSchema.parse(data.get("percentage"), int | float),
            participants=BaseSchema.parse(
                data.get("participants"), typing.List[UserId]
            ),
            money=BaseSchema.parse(data.get("money"), None | int),
            items=BaseSchema.parse(
                data.get("items"), typing.List[FactionOcHistoryItem]
            ),
            destination=BaseSchema.parse(
                data.get("destination"), None | FactionOcHistoryPayoutDestinationEnum
            ),
        )

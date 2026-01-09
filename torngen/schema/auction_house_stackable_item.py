import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .item_uid import ItemUid
from .torn_item_type_enum import TornItemTypeEnum


@dataclass
class AuctionHouseStackableItem(BaseSchema):
    """
    JSON object of `AuctionHouseStackableItem`.
    """

    uid: ItemUid
    type: TornItemTypeEnum
    name: str
    id: ItemId

    @staticmethod
    def parse(data):
        return AuctionHouseStackableItem(
            uid=BaseSchema.parse(data.get("uid"), ItemUid),
            type=BaseSchema.parse(data.get("type"), TornItemTypeEnum),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .torn_racket_type import TornRacketType


@dataclass
class TornRacketReward(BaseSchema):
    """
    JSON object of `TornRacketReward`.
    """

    type: TornRacketType
    quantity: int
    id: None | ItemId

    @staticmethod
    def parse(data):
        return TornRacketReward(
            type=BaseSchema.parse(data.get("type"), TornRacketType),
            quantity=BaseSchema.parse(data.get("quantity"), int),
            id=BaseSchema.parse(data.get("id"), None | ItemId),
        )

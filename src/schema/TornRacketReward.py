import typing

from ItemId import ItemId
from TornRacketType import TornRacketType

from ..base_schema import BaseSchema


class TornRacketReward(BaseSchema):

    type: TornRacketType
    quantity: int
    id: None | ItemId

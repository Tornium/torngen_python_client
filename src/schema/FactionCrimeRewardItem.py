import typing

from ItemId import ItemId

from ..base_schema import BaseSchema


class FactionCrimeRewardItem(BaseSchema):

    quantity: int
    id: ItemId

import typing

from AmmoId import AmmoId
from TornItemAmmoTypeEnum import TornItemAmmoTypeEnum

from ..base_schema import BaseSchema


class TornItemAmmo(BaseSchema):

    types: typing.List[TornItemAmmoTypeEnum]
    price: int
    name: str
    id: AmmoId

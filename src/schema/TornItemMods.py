import typing

from ItemModId import ItemModId
from TornItemWeaponTypeEnum import TornItemWeaponTypeEnum

from ..base_schema import BaseSchema


class TornItemMods(BaseSchema):

    weapons: typing.List[TornItemWeaponTypeEnum]
    name: str
    id: ItemModId
    dual_fit: bool
    description: str

import typing

from AmmoId import AmmoId
from ItemModId import ItemModId
from TornItemBaseStats import TornItemBaseStats
from TornItemWeaponCategoryEnum import TornItemWeaponCategoryEnum

from ..base_schema import BaseSchema


class TornItemWeaponDetails(BaseSchema):

    stealth_level: int | float
    mods: typing.List[ItemModId]
    category: TornItemWeaponCategoryEnum
    base_stats: TornItemBaseStats
    ammo: None | typing.TypedDict(
        "",
        {
            "rate_of_fire": typing.TypedDict("", {"minimum": int, "maximum": int}),
            "name": str,
            "magazine_rounds": int,
            "id": AmmoId,
        },
    )

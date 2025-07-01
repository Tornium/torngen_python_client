import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .ammo_id import AmmoId
from .item_mod_id import ItemModId
from .torn_item_base_stats import TornItemBaseStats
from .torn_item_weapon_category_enum import TornItemWeaponCategoryEnum


@dataclass
class TornItemWeaponDetails(BaseSchema):
    """
    JSON object of `TornItemWeaponDetails`.
    """

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

    @staticmethod
    def parse(data):
        return TornItemWeaponDetails(
            stealth_level=BaseSchema.parse(data.get("stealth_level"), int | float),
            mods=BaseSchema.parse(data.get("mods"), typing.List[ItemModId]),
            category=BaseSchema.parse(data.get("category"), TornItemWeaponCategoryEnum),
            base_stats=BaseSchema.parse(data.get("base_stats"), TornItemBaseStats),
            ammo=BaseSchema.parse(
                data.get("ammo"),
                None
                | typing.TypedDict(
                    "",
                    {
                        "rate_of_fire": typing.TypedDict(
                            "", {"minimum": int, "maximum": int}
                        ),
                        "name": str,
                        "magazine_rounds": int,
                        "id": AmmoId,
                    },
                ),
            ),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .torn_item_armor_details import TornItemArmorDetails
from .torn_item_type_enum import TornItemTypeEnum
from .torn_item_weapon_details import TornItemWeaponDetails
from .torn_item_weapon_type_enum import TornItemWeaponTypeEnum


@dataclass
class TornItem(BaseSchema):
    """
    JSON object of `TornItem`.
    """

    value: typing.TypedDict(
        "",
        {
            "vendor": None | typing.TypedDict("", {"name": str, "country": str}),
            "sell_price": None | int,
            "market_price": int,
            "buy_price": None | int,
        },
    )
    type: TornItemTypeEnum
    sub_type: None | TornItemWeaponTypeEnum
    requirement: None | str
    name: str
    is_tradable: bool
    is_masked: bool
    is_found_in_city: bool
    image: str
    id: ItemId
    effect: None | str
    details: None | TornItemArmorDetails | TornItemWeaponDetails
    description: str
    circulation: int

    @staticmethod
    def parse(data):
        return TornItem(
            value=BaseSchema.parse(
                data.get("value"),
                typing.TypedDict(
                    "",
                    {
                        "vendor": None
                        | typing.TypedDict("", {"name": str, "country": str}),
                        "sell_price": None | int,
                        "market_price": int,
                        "buy_price": None | int,
                    },
                ),
            ),
            type=BaseSchema.parse(data.get("type"), TornItemTypeEnum),
            sub_type=BaseSchema.parse(
                data.get("sub_type"), None | TornItemWeaponTypeEnum
            ),
            requirement=BaseSchema.parse(data.get("requirement"), None | str),
            name=BaseSchema.parse(data.get("name"), str),
            is_tradable=BaseSchema.parse(data.get("is_tradable"), bool),
            is_masked=BaseSchema.parse(data.get("is_masked"), bool),
            is_found_in_city=BaseSchema.parse(data.get("is_found_in_city"), bool),
            image=BaseSchema.parse(data.get("image"), str),
            id=BaseSchema.parse(data.get("id"), ItemId),
            effect=BaseSchema.parse(data.get("effect"), None | str),
            details=BaseSchema.parse(
                data.get("details"), None | TornItemArmorDetails | TornItemWeaponDetails
            ),
            description=BaseSchema.parse(data.get("description"), str),
            circulation=BaseSchema.parse(data.get("circulation"), int),
        )

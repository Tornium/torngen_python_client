import typing

from ItemId import ItemId
from TornItemArmorDetails import TornItemArmorDetails
from TornItemTypeEnum import TornItemTypeEnum
from TornItemWeaponDetails import TornItemWeaponDetails
from TornItemWeaponTypeEnum import TornItemWeaponTypeEnum

from ..base_schema import BaseSchema


class TornItem(BaseSchema):

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

import typing

from RaceCarUpgradeCategory import RaceCarUpgradeCategory
from RaceCarUpgradeId import RaceCarUpgradeId
from RaceCarUpgradeSubCategory import RaceCarUpgradeSubCategory
from RaceClassEnum import RaceClassEnum

from ..base_schema import BaseSchema


class RaceCarUpgrade(BaseSchema):

    subcategory: RaceCarUpgradeSubCategory
    name: str
    id: RaceCarUpgradeId
    effects: typing.TypedDict(
        "",
        {
            "top_speed": int,
            "tarmac": int,
            "safety": int,
            "handling": int,
            "dirt": int,
            "braking": int,
            "acceleration": int,
        },
    )
    description: str
    cost: typing.TypedDict("", {"points": int, "cash": int})
    class_required: RaceClassEnum
    category: RaceCarUpgradeCategory

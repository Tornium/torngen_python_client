import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_car_upgrade_category import RaceCarUpgradeCategory
from .race_car_upgrade_id import RaceCarUpgradeId
from .race_car_upgrade_sub_category import RaceCarUpgradeSubCategory
from .race_class_enum import RaceClassEnum


@dataclass
class RaceCarUpgrade(BaseSchema):
    """
    JSON object of `RaceCarUpgrade`.
    """

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

    @staticmethod
    def parse(data):
        return RaceCarUpgrade(
            subcategory=BaseSchema.parse(
                data.get("subcategory"), RaceCarUpgradeSubCategory
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), RaceCarUpgradeId),
            effects=BaseSchema.parse(
                data.get("effects"),
                typing.TypedDict(
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
                ),
            ),
            description=BaseSchema.parse(data.get("description"), str),
            cost=BaseSchema.parse(
                data.get("cost"), typing.TypedDict("", {"points": int, "cash": int})
            ),
            class_required=BaseSchema.parse(data.get("class_required"), RaceClassEnum),
            category=BaseSchema.parse(data.get("category"), RaceCarUpgradeCategory),
        )

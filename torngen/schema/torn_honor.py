import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .honor_id import HonorId
from .honor_rarity_enum import HonorRarityEnum
from .honor_type_enum import HonorTypeEnum


@dataclass
class TornHonor(BaseSchema):
    """
    JSON object of `TornHonor`.
    """

    type: typing.TypedDict("", {"title": HonorTypeEnum, "id": int})
    rarity: typing.Optional[HonorRarityEnum]
    name: str
    id: HonorId
    equipped: typing.Optional[int]
    description: str
    circulation: typing.Optional[int]

    @staticmethod
    def parse(data):
        return TornHonor(
            type=BaseSchema.parse(
                data.get("type"),
                typing.TypedDict("", {"title": HonorTypeEnum, "id": int}),
            ),
            rarity=BaseSchema.parse(
                data.get("rarity"), typing.Optional[HonorRarityEnum]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), HonorId),
            equipped=BaseSchema.parse(data.get("equipped"), typing.Optional[int]),
            description=BaseSchema.parse(data.get("description"), str),
            circulation=BaseSchema.parse(data.get("circulation"), typing.Optional[int]),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .award_crimes_version_enum import AwardCrimesVersionEnum
from .honor_rarity_enum import HonorRarityEnum
from .medal_id import MedalId
from .medal_type_enum import MedalTypeEnum


@dataclass
class TornMedal(BaseSchema):
    """
    JSON object of `TornMedal`.
    """

    type: typing.TypedDict("", {"title": MedalTypeEnum, "id": str})
    rarity: HonorRarityEnum
    name: str
    id: MedalId
    description: str
    crimes_version: typing.Optional[AwardCrimesVersionEnum]
    circulation: int

    @staticmethod
    def parse(data):
        return TornMedal(
            type=BaseSchema.parse(
                data.get("type"),
                typing.TypedDict("", {"title": MedalTypeEnum, "id": str}),
            ),
            rarity=BaseSchema.parse(data.get("rarity"), HonorRarityEnum),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), MedalId),
            description=BaseSchema.parse(data.get("description"), str),
            crimes_version=BaseSchema.parse(
                data.get("crimes_version"), typing.Optional[AwardCrimesVersionEnum]
            ),
            circulation=BaseSchema.parse(data.get("circulation"), int),
        )

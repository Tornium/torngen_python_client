import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_position_ability_enum import FactionPositionAbilityEnum


@dataclass
class FactionPosition(BaseSchema):
    """
    JSON object of `FactionPosition`.
    """

    name: str
    is_default: bool
    abilities: typing.List[FactionPositionAbilityEnum]

    @staticmethod
    def parse(data):
        return FactionPosition(
            name=BaseSchema.parse(data.get("name"), str),
            is_default=BaseSchema.parse(data.get("is_default"), bool),
            abilities=BaseSchema.parse(
                data.get("abilities"), typing.List[FactionPositionAbilityEnum]
            ),
        )

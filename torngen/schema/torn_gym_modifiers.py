import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornGymModifiers(BaseSchema):
    """
    JSON object of `TornGymModifiers`.
    """

    strength: int | float
    speed: int | float
    dexterity: int | float
    defense: int | float

    @staticmethod
    def parse(data):
        return TornGymModifiers(
            strength=BaseSchema.parse(data.get("strength"), int | float),
            speed=BaseSchema.parse(data.get("speed"), int | float),
            dexterity=BaseSchema.parse(data.get("dexterity"), int | float),
            defense=BaseSchema.parse(data.get("defense"), int | float),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .gym_class_enum import GymClassEnum
from .gym_id import GymId
from .torn_gym_modifiers import TornGymModifiers


@dataclass
class TornGym(BaseSchema):
    """
    JSON object of `TornGym`.
    """

    note: None | str
    name: str
    modifiers: TornGymModifiers
    id: GymId
    energy_cost: int
    cost: int
    class_: GymClassEnum

    @staticmethod
    def parse(data):
        return TornGym(
            note=BaseSchema.parse(data.get("note"), None | str),
            name=BaseSchema.parse(data.get("name"), str),
            modifiers=BaseSchema.parse(data.get("modifiers"), TornGymModifiers),
            id=BaseSchema.parse(data.get("id"), GymId),
            energy_cost=BaseSchema.parse(data.get("energy_cost"), int),
            cost=BaseSchema.parse(data.get("cost"), int),
            class_=BaseSchema.parse(data.get("class"), GymClassEnum),
        )

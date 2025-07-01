import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_class_enum import RaceClassEnum


@dataclass
class RaceCar(BaseSchema):
    """
    JSON object of `RaceCar`.
    """

    top_speed: int
    tarmac: int
    safety: int
    handling: int
    dirt: int
    class_: RaceClassEnum
    car_item_name: str
    car_item_id: ItemId
    braking: int
    acceleration: int

    @staticmethod
    def parse(data):
        return RaceCar(
            top_speed=BaseSchema.parse(data.get("top_speed"), int),
            tarmac=BaseSchema.parse(data.get("tarmac"), int),
            safety=BaseSchema.parse(data.get("safety"), int),
            handling=BaseSchema.parse(data.get("handling"), int),
            dirt=BaseSchema.parse(data.get("dirt"), int),
            class_=BaseSchema.parse(data.get("class_"), RaceClassEnum),
            car_item_name=BaseSchema.parse(data.get("car_item_name"), str),
            car_item_id=BaseSchema.parse(data.get("car_item_id"), ItemId),
            braking=BaseSchema.parse(data.get("braking"), int),
            acceleration=BaseSchema.parse(data.get("acceleration"), int),
        )

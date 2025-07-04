import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_car_id import RaceCarId
from .race_car_upgrade_id import RaceCarUpgradeId
from .race_class_enum import RaceClassEnum


@dataclass
class UserRaceCarDetails(BaseSchema):

    worth: int
    races_won: int
    races_entered: int
    points_spent: int
    parts: typing.List[RaceCarUpgradeId]
    name: None | str
    is_removed: bool
    id: RaceCarId
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
        return UserRaceCarDetails(
            worth=BaseSchema.parse(data.get("worth"), int),
            races_won=BaseSchema.parse(data.get("races_won"), int),
            races_entered=BaseSchema.parse(data.get("races_entered"), int),
            points_spent=BaseSchema.parse(data.get("points_spent"), int),
            parts=BaseSchema.parse(data.get("parts"), typing.List[RaceCarUpgradeId]),
            name=BaseSchema.parse(data.get("name"), None | str),
            is_removed=BaseSchema.parse(data.get("is_removed"), bool),
            id=BaseSchema.parse(data.get("id"), RaceCarId),
            top_speed=BaseSchema.parse(data.get("top_speed"), int),
            tarmac=BaseSchema.parse(data.get("tarmac"), int),
            safety=BaseSchema.parse(data.get("safety"), int),
            handling=BaseSchema.parse(data.get("handling"), int),
            dirt=BaseSchema.parse(data.get("dirt"), int),
            class_=BaseSchema.parse(data.get("class"), RaceClassEnum),
            car_item_name=BaseSchema.parse(data.get("car_item_name"), str),
            car_item_id=BaseSchema.parse(data.get("car_item_id"), ItemId),
            braking=BaseSchema.parse(data.get("braking"), int),
            acceleration=BaseSchema.parse(data.get("acceleration"), int),
        )

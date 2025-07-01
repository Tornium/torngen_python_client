import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .race_car_id import RaceCarId
from .race_class_enum import RaceClassEnum
from .user_id import UserId


@dataclass
class RacerDetails(BaseSchema):
    """
    JSON object of `RacerDetails`.
    """

    time_ended: None | int
    race_time: None | int | float
    position: None | int
    has_crashed: None | bool
    driver_id: UserId
    car_item_name: str
    car_item_id: ItemId
    car_id: RaceCarId
    car_class: RaceClassEnum
    best_lap_time: None | int | float

    @staticmethod
    def parse(data):
        return RacerDetails(
            time_ended=BaseSchema.parse(data.get("time_ended"), None | int),
            race_time=BaseSchema.parse(data.get("race_time"), None | int | float),
            position=BaseSchema.parse(data.get("position"), None | int),
            has_crashed=BaseSchema.parse(data.get("has_crashed"), None | bool),
            driver_id=BaseSchema.parse(data.get("driver_id"), UserId),
            car_item_name=BaseSchema.parse(data.get("car_item_name"), str),
            car_item_id=BaseSchema.parse(data.get("car_item_id"), ItemId),
            car_id=BaseSchema.parse(data.get("car_id"), RaceCarId),
            car_class=BaseSchema.parse(data.get("car_class"), RaceClassEnum),
            best_lap_time=BaseSchema.parse(
                data.get("best_lap_time"), None | int | float
            ),
        )

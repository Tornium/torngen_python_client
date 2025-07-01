import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId
from .user_id import UserId


@dataclass
class RaceRecord(BaseSchema):
    """
    JSON object of `RaceRecord`.
    """

    lap_time: int | float
    driver_name: str
    driver_id: UserId
    car_item_name: str
    car_item_id: ItemId

    @staticmethod
    def parse(data):
        return RaceRecord(
            lap_time=BaseSchema.parse(data.get("lap_time"), int | float),
            driver_name=BaseSchema.parse(data.get("driver_name"), str),
            driver_id=BaseSchema.parse(data.get("driver_id"), UserId),
            car_item_name=BaseSchema.parse(data.get("car_item_name"), str),
            car_item_id=BaseSchema.parse(data.get("car_item_id"), ItemId),
        )

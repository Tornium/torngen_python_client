import typing

from ItemId import ItemId
from RaceCarId import RaceCarId
from RaceClassEnum import RaceClassEnum
from UserId import UserId

from ..base_schema import BaseSchema


class RacerDetails(BaseSchema):

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

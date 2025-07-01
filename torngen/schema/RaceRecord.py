import typing

from ItemId import ItemId
from UserId import UserId

from ..base_schema import BaseSchema


class RaceRecord(BaseSchema):

    lap_time: int | float
    driver_name: str
    driver_id: UserId
    car_item_name: str
    car_item_id: ItemId

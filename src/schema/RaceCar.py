import typing

from ItemId import ItemId
from RaceClassEnum import RaceClassEnum

from ..base_schema import BaseSchema


class RaceCar(BaseSchema):

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

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_car import RaceCar


@dataclass
class RacingCarsResponse(BaseSchema):
    """
    JSON object of `RacingCarsResponse`.
    """

    cars: typing.List[RaceCar]

    @staticmethod
    def parse(data):
        return RacingCarsResponse(
            cars=BaseSchema.parse(data.get("cars"), typing.List[RaceCar]),
        )

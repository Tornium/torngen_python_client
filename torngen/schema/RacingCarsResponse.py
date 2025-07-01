import typing

from RaceCar import RaceCar

from ..base_schema import BaseSchema


class RacingCarsResponse(BaseSchema):

    cars: typing.List[RaceCar]

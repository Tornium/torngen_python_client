import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_race_car_details import UserRaceCarDetails


@dataclass
class UserEnlistedCarsResponse(BaseSchema):
    """
    JSON object of `UserEnlistedCarsResponse`.
    """

    enlistedcars: typing.List[UserRaceCarDetails]

    @staticmethod
    def parse(data):
        return UserEnlistedCarsResponse(
            enlistedcars=BaseSchema.parse(
                data.get("enlistedcars"), typing.List[UserRaceCarDetails]
            ),
        )

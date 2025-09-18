import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .country_enum import CountryEnum
from .user_fly_method_enum import UserFlyMethodEnum


@dataclass
class UserTravelResponse(BaseSchema):
    """
    JSON object of `UserTravelResponse`.
    """

    travel: typing.TypedDict(
        "",
        {
            "time_left": int,
            "method": None | UserFlyMethodEnum,
            "destination": CountryEnum,
            "departed_at": None | int,
            "arrival_at": None | int,
        },
    )

    @staticmethod
    def parse(data):
        return UserTravelResponse(
            travel=BaseSchema.parse(
                data.get("travel"),
                typing.TypedDict(
                    "",
                    {
                        "time_left": int,
                        "method": None | UserFlyMethodEnum,
                        "destination": CountryEnum,
                        "departed_at": None | int,
                        "arrival_at": None | int,
                    },
                ),
            ),
        )

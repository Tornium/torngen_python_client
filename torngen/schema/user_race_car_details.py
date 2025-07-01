import typing

from ..base_schema import BaseSchema
from .race_car import RaceCar
from .race_car_id import RaceCarId
from .race_car_upgrade_id import RaceCarUpgradeId


class UserRaceCarDetails(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "",
            {
                "worth": int,
                "races_won": int,
                "races_entered": int,
                "points_spent": int,
                "parts": typing.List[RaceCarUpgradeId],
                "name": None | str,
                "is_removed": bool,
                "id": RaceCarId,
            },
        )
        | RaceCar
    ]

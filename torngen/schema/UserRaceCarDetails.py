import typing

from RaceCar import RaceCar
from RaceCarId import RaceCarId
from RaceCarUpgradeId import RaceCarUpgradeId

from ..base_schema import BaseSchema


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

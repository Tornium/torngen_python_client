import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_car_upgrade import RaceCarUpgrade


@dataclass
class RacingCarUpgradesResponse(BaseSchema):
    """
    JSON object of `RacingCarUpgradesResponse`.
    """

    carupgrades: typing.List[RaceCarUpgrade]

    @staticmethod
    def parse(data):
        return RacingCarUpgradesResponse(
            carupgrades=BaseSchema.parse(
                data.get("carupgrades"), typing.List[RaceCarUpgrade]
            ),
        )

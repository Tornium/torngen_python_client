import typing

from RaceCarUpgrade import RaceCarUpgrade

from ..base_schema import BaseSchema


class RacingCarUpgradesResponse(BaseSchema):

    carupgrades: typing.List[RaceCarUpgrade]

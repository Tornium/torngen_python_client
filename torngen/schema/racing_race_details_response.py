import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race import Race
from .racer_details import RacerDetails


@dataclass
class RacingRaceDetailsResponse(BaseSchema):
    """
    JSON object of `RacingRaceDetailsResponse`.
    """

    race: typing.List[
        typing.TypedDict(
            "", {"results": typing.List[RacerDetails], "is_official": bool}
        )
        | Race
    ]

    @staticmethod
    def parse(data):
        return RacingRaceDetailsResponse(
            race=BaseSchema.parse(
                data.get("race"),
                typing.List[
                    typing.TypedDict(
                        "", {"results": typing.List[RacerDetails], "is_official": bool}
                    )
                    | Race
                ],
            ),
        )

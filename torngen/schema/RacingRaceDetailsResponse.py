import typing

from Race import Race
from RacerDetails import RacerDetails

from ..base_schema import BaseSchema


class RacingRaceDetailsResponse(BaseSchema):

    race: typing.List[
        typing.TypedDict(
            "", {"results": typing.List[RacerDetails], "is_official": bool}
        )
        | Race
    ]

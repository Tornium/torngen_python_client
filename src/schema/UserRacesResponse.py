import typing

from RacingRaceDetailsResponse import RacingRaceDetailsResponse
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class UserRacesResponse(BaseSchema):

    races: typing.List[RacingRaceDetailsResponse]
    _metadata: RequestMetadataWithLinks

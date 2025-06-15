import typing

from Race import Race
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class RacingRacesResponse(BaseSchema):

    races: typing.List[Race]
    _metadata: RequestMetadataWithLinks

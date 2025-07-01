import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from TornTerritory import TornTerritory

from ..base_schema import BaseSchema


class TornTerritoriesResponse(BaseSchema):

    territory: typing.List[TornTerritory]
    _metadata: RequestMetadataWithLinks

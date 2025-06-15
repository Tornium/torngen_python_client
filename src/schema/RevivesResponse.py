import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from Revive import Revive

from ..base_schema import BaseSchema


class RevivesResponse(BaseSchema):

    revives: typing.List[Revive]
    _metadata: RequestMetadataWithLinks

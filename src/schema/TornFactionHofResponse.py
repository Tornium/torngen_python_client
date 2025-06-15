import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from TornFactionHof import TornFactionHof

from ..base_schema import BaseSchema


class TornFactionHofResponse(BaseSchema):

    factionhof: typing.List[TornFactionHof]
    _metadata: RequestMetadataWithLinks

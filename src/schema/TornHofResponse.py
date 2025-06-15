import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from TornHof import TornHof

from ..base_schema import BaseSchema


class TornHofResponse(BaseSchema):

    hof: typing.List[TornHof]
    _metadata: RequestMetadataWithLinks

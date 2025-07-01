import typing

from FactionCrime import FactionCrime
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionCrimesResponse(BaseSchema):

    crimes: typing.List[FactionCrime]
    _metadata: RequestMetadataWithLinks

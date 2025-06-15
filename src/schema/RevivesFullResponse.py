import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from ReviveSimplified import ReviveSimplified

from ..base_schema import BaseSchema


class RevivesFullResponse(BaseSchema):

    revives: typing.List[ReviveSimplified]
    _metadata: RequestMetadataWithLinks

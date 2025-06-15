import typing

from FactionRaidWarfare import FactionRaidWarfare
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionRaidsResponse(BaseSchema):

    raids: typing.List[FactionRaidWarfare]
    _metadata: RequestMetadataWithLinks

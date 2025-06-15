import typing

from Attack import Attack
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionAttacksResponse(BaseSchema):

    attacks: typing.List[Attack]
    _metadata: RequestMetadataWithLinks

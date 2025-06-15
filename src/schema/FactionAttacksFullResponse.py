import typing

from AttackSimplified import AttackSimplified
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionAttacksFullResponse(BaseSchema):

    attacks: typing.List[AttackSimplified]
    _metadata: RequestMetadataWithLinks

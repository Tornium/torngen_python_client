import typing

from AttackLog import AttackLog
from AttackLogSummary import AttackLogSummary
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class AttackLogResponse(BaseSchema):

    attacklog: typing.TypedDict(
        "", {"summary": typing.List[AttackLogSummary], "log": typing.List[AttackLog]}
    )
    _metadata: RequestMetadataWithLinks

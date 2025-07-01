import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_log import AttackLog
from .attack_log_summary import AttackLogSummary
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class AttackLogResponse(BaseSchema):
    """
    JSON object of `AttackLogResponse`.
    """

    attacklog: typing.TypedDict(
        "", {"summary": typing.List[AttackLogSummary], "log": typing.List[AttackLog]}
    )
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return AttackLogResponse(
            attacklog=BaseSchema.parse(
                data.get("attacklog"),
                typing.TypedDict(
                    "",
                    {
                        "summary": typing.List[AttackLogSummary],
                        "log": typing.List[AttackLog],
                    },
                ),
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .report import Report
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class ReportsResponse(BaseSchema):
    """
    JSON object of `ReportsResponse`.
    """

    reports: typing.List[Report]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return ReportsResponse(
            reports=BaseSchema.parse(data.get("reports"), typing.List[Report]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

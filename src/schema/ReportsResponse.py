import typing

from Report import Report
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class ReportsResponse(BaseSchema):

    reports: typing.List[Report]
    _metadata: RequestMetadataWithLinks

import typing

from FactionChainReport import FactionChainReport

from ..base_schema import BaseSchema


class FactionChainReportResponse(BaseSchema):

    chainreport: FactionChainReport

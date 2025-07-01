import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_chain_report import FactionChainReport


@dataclass
class FactionChainReportResponse(BaseSchema):
    """
    JSON object of `FactionChainReportResponse`.
    """

    chainreport: FactionChainReport

    @staticmethod
    def parse(data):
        return FactionChainReportResponse(
            chainreport=BaseSchema.parse(data.get("chainreport"), FactionChainReport),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_report import FactionRaidReport


@dataclass
class FactionRaidWarReportResponse(BaseSchema):
    """
    JSON object of `FactionRaidWarReportResponse`.
    """

    raidreport: typing.List[FactionRaidReport]

    @staticmethod
    def parse(data):
        return FactionRaidWarReportResponse(
            raidreport=BaseSchema.parse(
                data.get("raidreport"), typing.List[FactionRaidReport]
            ),
        )

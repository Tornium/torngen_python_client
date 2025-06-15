import typing

from FactionRaidReportFaction import FactionRaidReportFaction
from RaidWarId import RaidWarId

from ..base_schema import BaseSchema


class FactionRaidReport(BaseSchema):

    start: int
    id: RaidWarId
    end: int
    defender: FactionRaidReportFaction
    aggressor: FactionRaidReportFaction

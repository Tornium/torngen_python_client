import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_report_faction import FactionRaidReportFaction
from .raid_war_id import RaidWarId


@dataclass
class FactionRaidReport(BaseSchema):
    """
    JSON object of `FactionRaidReport`.
    """

    start: int
    id: RaidWarId
    end: int
    defender: FactionRaidReportFaction
    aggressor: FactionRaidReportFaction

    @staticmethod
    def parse(data):
        return FactionRaidReport(
            start=BaseSchema.parse(data.get("start"), int),
            id=BaseSchema.parse(data.get("id"), RaidWarId),
            end=BaseSchema.parse(data.get("end"), int),
            defender=BaseSchema.parse(data.get("defender"), FactionRaidReportFaction),
            aggressor=BaseSchema.parse(data.get("aggressor"), FactionRaidReportFaction),
        )

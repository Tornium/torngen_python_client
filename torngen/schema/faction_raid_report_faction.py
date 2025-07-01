import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_raid_report_attacker import FactionRaidReportAttacker
from .faction_raid_report_user import FactionRaidReportUser


@dataclass
class FactionRaidReportFaction(BaseSchema):
    """
    JSON object of `FactionRaidReportFaction`.
    """

    score: int | float
    non_attackers: typing.List[FactionRaidReportUser]
    name: str
    id: FactionId
    attackers: typing.List[FactionRaidReportAttacker]

    @staticmethod
    def parse(data):
        return FactionRaidReportFaction(
            score=BaseSchema.parse(data.get("score"), int | float),
            non_attackers=BaseSchema.parse(
                data.get("non_attackers"), typing.List[FactionRaidReportUser]
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            attackers=BaseSchema.parse(
                data.get("attackers"), typing.List[FactionRaidReportAttacker]
            ),
        )

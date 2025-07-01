import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_report_user import FactionRaidReportUser


@dataclass
class FactionRaidReportAttacker(BaseSchema):
    """
    JSON object of `FactionRaidReportAttacker`.
    """

    user: FactionRaidReportUser
    damage: int | float
    attacks: int

    @staticmethod
    def parse(data):
        return FactionRaidReportAttacker(
            user=BaseSchema.parse(data.get("user"), FactionRaidReportUser),
            damage=BaseSchema.parse(data.get("damage"), int | float),
            attacks=BaseSchema.parse(data.get("attacks"), int),
        )

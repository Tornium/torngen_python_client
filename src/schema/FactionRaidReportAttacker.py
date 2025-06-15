import typing

from FactionRaidReportUser import FactionRaidReportUser

from ..base_schema import BaseSchema


class FactionRaidReportAttacker(BaseSchema):

    user: FactionRaidReportUser
    damage: int | float
    attacks: int

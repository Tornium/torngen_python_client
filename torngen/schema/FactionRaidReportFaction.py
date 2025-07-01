import typing

from FactionId import FactionId
from FactionRaidReportAttacker import FactionRaidReportAttacker
from FactionRaidReportUser import FactionRaidReportUser

from ..base_schema import BaseSchema


class FactionRaidReportFaction(BaseSchema):

    score: int | float
    non_attackers: typing.List[FactionRaidReportUser]
    name: str
    id: FactionId
    attackers: typing.List[FactionRaidReportAttacker]

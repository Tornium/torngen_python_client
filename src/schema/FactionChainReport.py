import typing

from ChainId import ChainId
from FactionChainReportAttacker import FactionChainReportAttacker
from FactionChainReportBonus import FactionChainReportBonus
from FactionChainReportDetails import FactionChainReportDetails
from FactionId import FactionId
from UserId import UserId

from ..base_schema import BaseSchema


class FactionChainReport(BaseSchema):

    start: int
    non_attackers: typing.List[UserId]
    id: ChainId
    faction_id: FactionId
    end: int
    details: FactionChainReportDetails
    bonuses: typing.List[FactionChainReportBonus]
    attackers: typing.List[FactionChainReportAttacker]

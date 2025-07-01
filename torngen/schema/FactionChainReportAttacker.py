import typing

from FactionChainReportAttackerAttacks import FactionChainReportAttackerAttacks
from FactionChainReportAttackerRespect import FactionChainReportAttackerRespect
from UserId import UserId

from ..base_schema import BaseSchema


class FactionChainReportAttacker(BaseSchema):

    respect: FactionChainReportAttackerRespect
    id: UserId
    attacks: FactionChainReportAttackerAttacks

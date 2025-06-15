import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionChainReportBonus(BaseSchema):

    respect: int
    defender_id: UserId
    chain: int
    attacker_id: UserId

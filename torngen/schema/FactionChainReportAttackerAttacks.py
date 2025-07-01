import typing

from ..base_schema import BaseSchema


class FactionChainReportAttackerAttacks(BaseSchema):

    war: int
    total: int
    retaliations: int
    overseas: int
    mug: int
    losses: int
    leave: int
    hospitalize: int
    escapes: int
    draws: int
    bonuses: int
    assists: int

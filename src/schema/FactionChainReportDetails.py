import typing

from ..base_schema import BaseSchema


class FactionChainReportDetails(BaseSchema):

    war: int
    targets: int
    retaliations: int
    respect: int | float
    overseas: int
    mug: int
    members: int
    losses: int
    leave: int
    hospitalize: int
    escapes: int
    draws: int
    chain: int
    best: int | float
    assists: int

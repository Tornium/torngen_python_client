import typing

from ChainId import ChainId

from ..base_schema import BaseSchema


class FactionChain(BaseSchema):

    start: int
    respect: int | float
    id: ChainId
    end: int
    chain: int

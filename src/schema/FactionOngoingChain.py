import typing

from ChainId import ChainId

from ..base_schema import BaseSchema


class FactionOngoingChain(BaseSchema):

    timeout: int
    start: int
    modifier: int | float
    max: int
    id: ChainId
    end: int
    current: int
    cooldown: int

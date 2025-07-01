import typing

from FactionOngoingChain import FactionOngoingChain

from ..base_schema import BaseSchema


class FactionOngoingChainResponse(BaseSchema):

    chain: FactionOngoingChain

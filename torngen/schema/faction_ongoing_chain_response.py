import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_ongoing_chain import FactionOngoingChain


@dataclass
class FactionOngoingChainResponse(BaseSchema):
    """
    JSON object of `FactionOngoingChainResponse`.
    """

    chain: FactionOngoingChain

    @staticmethod
    def parse(data):
        return FactionOngoingChainResponse(
            chain=BaseSchema.parse(data.get("chain"), FactionOngoingChain),
        )

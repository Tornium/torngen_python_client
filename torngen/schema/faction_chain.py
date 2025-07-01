import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .chain_id import ChainId


@dataclass
class FactionChain(BaseSchema):
    """
    JSON object of `FactionChain`.
    """

    start: int
    respect: int | float
    id: ChainId
    end: int
    chain: int

    @staticmethod
    def parse(data):
        return FactionChain(
            start=BaseSchema.parse(data.get("start"), int),
            respect=BaseSchema.parse(data.get("respect"), int | float),
            id=BaseSchema.parse(data.get("id"), ChainId),
            end=BaseSchema.parse(data.get("end"), int),
            chain=BaseSchema.parse(data.get("chain"), int),
        )

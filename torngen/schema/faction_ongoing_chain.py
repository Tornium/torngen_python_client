import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .chain_id import ChainId


@dataclass
class FactionOngoingChain(BaseSchema):
    """
    JSON object of `FactionOngoingChain`.
    """

    timeout: int
    start: int
    modifier: int | float
    max: int
    id: ChainId
    end: int
    current: int
    cooldown: int

    @staticmethod
    def parse(data):
        return FactionOngoingChain(
            timeout=BaseSchema.parse(data.get("timeout"), int),
            start=BaseSchema.parse(data.get("start"), int),
            modifier=BaseSchema.parse(data.get("modifier"), int | float),
            max=BaseSchema.parse(data.get("max"), int),
            id=BaseSchema.parse(data.get("id"), ChainId),
            end=BaseSchema.parse(data.get("end"), int),
            current=BaseSchema.parse(data.get("current"), int),
            cooldown=BaseSchema.parse(data.get("cooldown"), int),
        )

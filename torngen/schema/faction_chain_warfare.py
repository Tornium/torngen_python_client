import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .chain_id import ChainId
from .faction_id import FactionId


@dataclass
class FactionChainWarfare(BaseSchema):

    faction: typing.TypedDict("", {"name": str, "id": FactionId})
    start: int
    respect: int | float
    id: ChainId
    end: int
    chain: int

    @staticmethod
    def parse(data):
        return FactionChainWarfare(
            faction=BaseSchema.parse(
                data.get("faction"),
                typing.TypedDict("", {"name": str, "id": FactionId}),
            ),
            start=BaseSchema.parse(data.get("start"), int),
            respect=BaseSchema.parse(data.get("respect"), int | float),
            id=BaseSchema.parse(data.get("id"), ChainId),
            end=BaseSchema.parse(data.get("end"), int),
            chain=BaseSchema.parse(data.get("chain"), int),
        )

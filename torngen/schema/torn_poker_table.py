import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .poker_table_id import PokerTableId


@dataclass
class TornPokerTable(BaseSchema):
    """
    JSON object of `TornPokerTable`.
    """

    speed: int
    players: typing.TypedDict("", {"maximum": int, "current": int})
    name: str
    id: PokerTableId
    blinds: typing.TypedDict("", {"small": int, "big": int})

    @staticmethod
    def parse(data):
        return TornPokerTable(
            speed=BaseSchema.parse(data.get("speed"), int),
            players=BaseSchema.parse(
                data.get("players"),
                typing.TypedDict("", {"maximum": int, "current": int}),
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), PokerTableId),
            blinds=BaseSchema.parse(
                data.get("blinds"), typing.TypedDict("", {"small": int, "big": int})
            ),
        )

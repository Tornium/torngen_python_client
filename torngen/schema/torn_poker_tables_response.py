import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_poker_table import TornPokerTable


@dataclass
class TornPokerTablesResponse(BaseSchema):
    """
    JSON object of `TornPokerTablesResponse`.
    """

    pokertables: typing.List[TornPokerTable]

    @staticmethod
    def parse(data):
        return TornPokerTablesResponse(
            pokertables=BaseSchema.parse(
                data.get("pokertables"), typing.List[TornPokerTable]
            ),
        )

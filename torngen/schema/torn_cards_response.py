import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_card import TornCard


@dataclass
class TornCardsResponse(BaseSchema):
    """
    JSON object of `TornCardsResponse`.
    """

    cards: typing.List[TornCard]

    @staticmethod
    def parse(data):
        return TornCardsResponse(
            cards=BaseSchema.parse(data.get("cards"), typing.List[TornCard]),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_racket import TornRacket


@dataclass
class FactionRacketsResponse(BaseSchema):
    """
    JSON object of `FactionRacketsResponse`.
    """

    rackets: typing.List[TornRacket]

    @staticmethod
    def parse(data):
        return FactionRacketsResponse(
            rackets=BaseSchema.parse(data.get("rackets"), typing.List[TornRacket]),
        )

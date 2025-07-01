import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_racket import TornRacket


@dataclass
class FactionRacketsReponse(BaseSchema):
    """
    JSON object of `FactionRacketsReponse`.
    """

    rackets: typing.List[TornRacket]

    @staticmethod
    def parse(data):
        return FactionRacketsReponse(
            rackets=BaseSchema.parse(data.get("rackets"), typing.List[TornRacket]),
        )

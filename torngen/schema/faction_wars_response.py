import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_pact import FactionPact
from .faction_wars import FactionWars


@dataclass
class FactionWarsResponse(BaseSchema):
    """
    JSON object of `FactionWarsResponse`.
    """

    wars: FactionWars
    pacts: typing.List[FactionPact]

    @staticmethod
    def parse(data):
        return FactionWarsResponse(
            wars=BaseSchema.parse(data.get("wars"), FactionWars),
            pacts=BaseSchema.parse(data.get("pacts"), typing.List[FactionPact]),
        )

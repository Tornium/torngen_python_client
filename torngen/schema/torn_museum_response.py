import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_museum_set import TornMuseumSet


@dataclass
class TornMuseumResponse(BaseSchema):
    """
    JSON object of `TornMuseumResponse`.
    """

    museum: typing.List[TornMuseumSet]

    @staticmethod
    def parse(data):
        return TornMuseumResponse(
            museum=BaseSchema.parse(data.get("museum"), typing.List[TornMuseumSet]),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_medal import TornMedal


@dataclass
class TornMedalsResponse(BaseSchema):
    """
    JSON object of `TornMedalsResponse`.
    """

    medals: typing.List[TornMedal]

    @staticmethod
    def parse(data):
        return TornMedalsResponse(
            medals=BaseSchema.parse(data.get("medals"), typing.List[TornMedal]),
        )

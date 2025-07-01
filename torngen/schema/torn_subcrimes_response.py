import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_subcrime import TornSubcrime


@dataclass
class TornSubcrimesResponse(BaseSchema):
    """
    JSON object of `TornSubcrimesResponse`.
    """

    subcrimes: typing.List[TornSubcrime]

    @staticmethod
    def parse(data):
        return TornSubcrimesResponse(
            subcrimes=BaseSchema.parse(
                data.get("subcrimes"), typing.List[TornSubcrime]
            ),
        )

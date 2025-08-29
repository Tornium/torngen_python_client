import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_merit import TornMerit


@dataclass
class TornMeritsResponse(BaseSchema):
    """
    JSON object of `TornMeritsResponse`.
    """

    merits: typing.List[TornMerit]

    @staticmethod
    def parse(data):
        return TornMeritsResponse(
            merits=BaseSchema.parse(data.get("merits"), typing.List[TornMerit]),
        )

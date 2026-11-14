import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_halloween import TornHalloween


@dataclass
class TornHalloweenResponse(BaseSchema):
    """
    JSON object of `TornHalloweenResponse`.
    """

    halloween: TornHalloween

    @staticmethod
    def parse(data):
        return TornHalloweenResponse(
            halloween=BaseSchema.parse(data.get("halloween"), TornHalloween),
        )

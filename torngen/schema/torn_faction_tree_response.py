import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_faction_tree import TornFactionTree


@dataclass
class TornFactionTreeResponse(BaseSchema):
    """
    JSON object of `TornFactionTreeResponse`.
    """

    factionTree: typing.List[TornFactionTree]

    @staticmethod
    def parse(data):
        return TornFactionTreeResponse(
            factionTree=BaseSchema.parse(
                data.get("factionTree"), typing.List[TornFactionTree]
            ),
        )

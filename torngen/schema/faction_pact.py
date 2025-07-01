import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class FactionPact(BaseSchema):
    """
    JSON object of `FactionPact`.
    """

    until: str
    faction_name: str
    faction_id: FactionId

    @staticmethod
    def parse(data):
        return FactionPact(
            until=BaseSchema.parse(data.get("until"), str),
            faction_name=BaseSchema.parse(data.get("faction_name"), str),
            faction_id=BaseSchema.parse(data.get("faction_id"), FactionId),
        )

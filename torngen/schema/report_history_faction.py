import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class ReportHistoryFaction(BaseSchema):
    """
    JSON object of `ReportHistoryFaction`.
    """

    name: str
    left: None | str
    joined: str
    id: FactionId

    @staticmethod
    def parse(data):
        return ReportHistoryFaction(
            name=BaseSchema.parse(data.get("name"), str),
            left=BaseSchema.parse(data.get("left"), None | str),
            joined=BaseSchema.parse(data.get("joined"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )

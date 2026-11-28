import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_id import FactionCrimeId
from .faction_oc_history_entry import FactionOcHistoryEntry


@dataclass
class FactionOcHistory(BaseSchema):
    """
    JSON object of `FactionOcHistory`.
    """

    history: typing.List[FactionOcHistoryEntry]
    crime_id: FactionCrimeId

    @staticmethod
    def parse(data):
        return FactionOcHistory(
            history=BaseSchema.parse(
                data.get("history"), typing.List[FactionOcHistoryEntry]
            ),
            crime_id=BaseSchema.parse(data.get("crime_id"), FactionCrimeId),
        )

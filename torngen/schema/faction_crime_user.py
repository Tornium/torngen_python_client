import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_user_item_outcome import FactionCrimeUserItemOutcome
from .faction_crime_user_outcome import FactionCrimeUserOutcome
from .user_id import UserId


@dataclass
class FactionCrimeUser(BaseSchema):
    """
    JSON object of `FactionCrimeUser`.
    """

    progress: int | float
    outcome_duration: None | int
    outcome: None | FactionCrimeUserOutcome
    joined_at: int
    item_outcome: None | FactionCrimeUserItemOutcome
    id: UserId

    @staticmethod
    def parse(data):
        return FactionCrimeUser(
            progress=BaseSchema.parse(data.get("progress"), int | float),
            outcome_duration=BaseSchema.parse(data.get("outcome_duration"), None | int),
            outcome=BaseSchema.parse(
                data.get("outcome"), None | FactionCrimeUserOutcome
            ),
            joined_at=BaseSchema.parse(data.get("joined_at"), int),
            item_outcome=BaseSchema.parse(
                data.get("item_outcome"), None | FactionCrimeUserItemOutcome
            ),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

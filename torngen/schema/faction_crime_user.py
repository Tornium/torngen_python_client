import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_user_outcome import FactionCrimeUserOutcome
from .user_id import UserId


@dataclass
class FactionCrimeUser(BaseSchema):
    """
    JSON object of `FactionCrimeUser`.
    """

    progress: int | float
    outcome: None | FactionCrimeUserOutcome
    joined_at: int
    id: UserId

    @staticmethod
    def parse(data):
        return FactionCrimeUser(
            progress=BaseSchema.parse(data.get("progress"), int | float),
            outcome=BaseSchema.parse(
                data.get("outcome"), None | FactionCrimeUserOutcome
            ),
            joined_at=BaseSchema.parse(data.get("joined_at"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

import typing

from FactionCrimeUserOutcome import FactionCrimeUserOutcome
from UserId import UserId

from ..base_schema import BaseSchema


class FactionCrimeUser(BaseSchema):

    progress: int | float
    outcome: None | FactionCrimeUserOutcome
    joined_at: int
    id: UserId

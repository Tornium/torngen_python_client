import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .medal_id import MedalId


@dataclass
class UserMedal(BaseSchema):
    """
    JSON object of `UserMedal`.
    """

    timestamp: int
    id: MedalId

    @staticmethod
    def parse(data):
        return UserMedal(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), MedalId),
        )

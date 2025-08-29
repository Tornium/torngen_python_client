import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .merit_id import MeritId


@dataclass
class UserMeritUpgrade(BaseSchema):
    """
    JSON object of `UserMeritUpgrade`.
    """

    level: int
    id: MeritId

    @staticmethod
    def parse(data):
        return UserMeritUpgrade(
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), MeritId),
        )

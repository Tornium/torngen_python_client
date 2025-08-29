import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .honor_id import HonorId


@dataclass
class UserHonor(BaseSchema):
    """
    JSON object of `UserHonor`.
    """

    timestamp: int
    id: HonorId

    @staticmethod
    def parse(data):
        return UserHonor(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            id=BaseSchema.parse(data.get("id"), HonorId),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserLastAction(BaseSchema):
    """
    JSON object of `UserLastAction`.
    """

    timestamp: int
    status: str
    relative: str

    @staticmethod
    def parse(data):
        return UserLastAction(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            status=BaseSchema.parse(data.get("status"), str),
            relative=BaseSchema.parse(data.get("relative"), str),
        )

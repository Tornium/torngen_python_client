import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class News(BaseSchema):
    """
    JSON object of `News`.
    """

    timestamp: int
    text: str
    id: str

    @staticmethod
    def parse(data):
        return News(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            text=BaseSchema.parse(data.get("text"), str),
            id=BaseSchema.parse(data.get("id"), str),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionNews(BaseSchema):
    """
    JSON object of `FactionNews`.
    """

    timestamp: int
    text: str
    id: str

    @staticmethod
    def parse(data):
        return FactionNews(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            text=BaseSchema.parse(data.get("text"), str),
            id=BaseSchema.parse(data.get("id"), str),
        )

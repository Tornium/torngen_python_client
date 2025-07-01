import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TimestampResponse(BaseSchema):
    """
    JSON object of `TimestampResponse`.
    """

    timestamp: int

    @staticmethod
    def parse(data):
        return TimestampResponse(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
        )

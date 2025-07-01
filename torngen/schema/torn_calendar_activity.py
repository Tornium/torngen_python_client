import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornCalendarActivity(BaseSchema):
    """
    JSON object of `TornCalendarActivity`.
    """

    title: str
    start: int
    end: int
    description: str

    @staticmethod
    def parse(data):
        return TornCalendarActivity(
            title=BaseSchema.parse(data.get("title"), str),
            start=BaseSchema.parse(data.get("start"), int),
            end=BaseSchema.parse(data.get("end"), int),
            description=BaseSchema.parse(data.get("description"), str),
        )

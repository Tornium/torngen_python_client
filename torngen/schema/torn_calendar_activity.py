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
    latest_end: int
    fixed_start_time: bool
    end: int
    earliest_start: int
    description: str

    @staticmethod
    def parse(data):
        return TornCalendarActivity(
            title=BaseSchema.parse(data.get("title"), str),
            start=BaseSchema.parse(data.get("start"), int),
            latest_end=BaseSchema.parse(data.get("latest_end"), int),
            fixed_start_time=BaseSchema.parse(data.get("fixed_start_time"), bool),
            end=BaseSchema.parse(data.get("end"), int),
            earliest_start=BaseSchema.parse(data.get("earliest_start"), int),
            description=BaseSchema.parse(data.get("description"), str),
        )

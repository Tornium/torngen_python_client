import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCalendar(BaseSchema):
    """
    JSON object of `UserCalendar`.
    """

    start_time: str

    @staticmethod
    def parse(data):
        return UserCalendar(
            start_time=BaseSchema.parse(data.get("start_time"), str),
        )

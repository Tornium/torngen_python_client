import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserBar(BaseSchema):
    """
    JSON object of `UserBar`.
    """

    tick_time: int
    maximum: int
    interval: int
    increment: int
    full_time: int
    current: int

    @staticmethod
    def parse(data):
        return UserBar(
            tick_time=BaseSchema.parse(data.get("tick_time"), int),
            maximum=BaseSchema.parse(data.get("maximum"), int),
            interval=BaseSchema.parse(data.get("interval"), int),
            increment=BaseSchema.parse(data.get("increment"), int),
            full_time=BaseSchema.parse(data.get("full_time"), int),
            current=BaseSchema.parse(data.get("current"), int),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserBar(BaseSchema):
    """
    JSON object of `UserBar`.
    """

    maximum: int
    current: int

    @staticmethod
    def parse(data):
        return UserBar(
            maximum=BaseSchema.parse(data.get("maximum"), int),
            current=BaseSchema.parse(data.get("current"), int),
        )

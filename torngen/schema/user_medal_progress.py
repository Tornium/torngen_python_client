import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserMedalProgress(BaseSchema):
    """
    JSON object of `UserMedalProgress`.
    """

    target: int
    current: int

    @staticmethod
    def parse(data):
        return UserMedalProgress(
            target=BaseSchema.parse(data.get("target"), int),
            current=BaseSchema.parse(data.get("current"), int),
        )

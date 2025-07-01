import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserFactionBalance(BaseSchema):
    """
    JSON object of `UserFactionBalance`.
    """

    points: int
    money: int

    @staticmethod
    def parse(data):
        return UserFactionBalance(
            points=BaseSchema.parse(data.get("points"), int),
            money=BaseSchema.parse(data.get("money"), int),
        )

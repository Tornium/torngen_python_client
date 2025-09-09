import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCompetitionEasterEggs(BaseSchema):
    """
    JSON object of `UserCompetitionEasterEggs`.
    """

    total: int
    score: int
    name: typing.Literal["Easter Egg Hunt"]

    @staticmethod
    def parse(data):
        return UserCompetitionEasterEggs(
            total=BaseSchema.parse(data.get("total"), int),
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), typing.Literal["Easter Egg Hunt"]),
        )

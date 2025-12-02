import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCompetitionElimination(BaseSchema):
    """
    JSON object of `UserCompetitionElimination`.
    """

    team: typing.Optional[str]
    score: int
    name: typing.Literal["Elimination"]
    attacks: typing.Optional[int]

    @staticmethod
    def parse(data):
        return UserCompetitionElimination(
            team=BaseSchema.parse(data.get("team"), typing.Optional[str]),
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), typing.Literal["Elimination"]),
            attacks=BaseSchema.parse(data.get("attacks"), typing.Optional[int]),
        )

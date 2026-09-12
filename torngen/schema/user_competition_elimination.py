import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .elimination_team_id import EliminationTeamId


@dataclass
class UserCompetitionElimination(BaseSchema):
    """
    JSON object of `UserCompetitionElimination`.
    """

    team_id: None | EliminationTeamId
    team: str
    score: int
    name: typing.Literal["Elimination"]
    attacks: int

    @staticmethod
    def parse(data):
        return UserCompetitionElimination(
            team_id=BaseSchema.parse(data.get("team_id"), None | EliminationTeamId),
            team=BaseSchema.parse(data.get("team"), str),
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), typing.Literal["Elimination"]),
            attacks=BaseSchema.parse(data.get("attacks"), int),
        )

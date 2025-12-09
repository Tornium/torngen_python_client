import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .elimination_team_id import EliminationTeamId


@dataclass
class TornEliminationTeam(BaseSchema):
    """
    JSON object of `TornEliminationTeam`.
    """

    wins: int
    score: int
    position: int
    participants: int
    name: str
    losses: int
    lives: int
    leaders: typing.List[BasicUser]
    id: EliminationTeamId
    eliminated_timestamp: None | int
    eliminated: bool

    @staticmethod
    def parse(data):
        return TornEliminationTeam(
            wins=BaseSchema.parse(data.get("wins"), int),
            score=BaseSchema.parse(data.get("score"), int),
            position=BaseSchema.parse(data.get("position"), int),
            participants=BaseSchema.parse(data.get("participants"), int),
            name=BaseSchema.parse(data.get("name"), str),
            losses=BaseSchema.parse(data.get("losses"), int),
            lives=BaseSchema.parse(data.get("lives"), int),
            leaders=BaseSchema.parse(data.get("leaders"), typing.List[BasicUser]),
            id=BaseSchema.parse(data.get("id"), EliminationTeamId),
            eliminated_timestamp=BaseSchema.parse(
                data.get("eliminated_timestamp"), None | int
            ),
            eliminated=BaseSchema.parse(data.get("eliminated"), bool),
        )

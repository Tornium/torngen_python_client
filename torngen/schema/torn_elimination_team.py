import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .elimination_team_id import EliminationTeamId
from .torn_elimination_team_attacks_summary import TornEliminationTeamAttacksSummary
from .torn_elimination_team_leader import TornEliminationTeamLeader


@dataclass
class TornEliminationTeam(BaseSchema):
    """
    JSON object of `TornEliminationTeam`.
    """

    wins: int
    score: int
    position: int
    participants_left: int
    participants: int
    name: str
    losses: int
    lives: int
    leaders: typing.TypedDict(
        "",
        {
            "vice_captains": typing.List[TornEliminationTeamLeader],
            "captain": None | TornEliminationTeamLeader,
        },
    )
    id: EliminationTeamId
    eliminated_timestamp: None | int
    eliminated: bool
    attacking_summary: typing.List[TornEliminationTeamAttacksSummary]

    @staticmethod
    def parse(data):
        return TornEliminationTeam(
            wins=BaseSchema.parse(data.get("wins"), int),
            score=BaseSchema.parse(data.get("score"), int),
            position=BaseSchema.parse(data.get("position"), int),
            participants_left=BaseSchema.parse(data.get("participants_left"), int),
            participants=BaseSchema.parse(data.get("participants"), int),
            name=BaseSchema.parse(data.get("name"), str),
            losses=BaseSchema.parse(data.get("losses"), int),
            lives=BaseSchema.parse(data.get("lives"), int),
            leaders=BaseSchema.parse(
                data.get("leaders"),
                typing.TypedDict(
                    "",
                    {
                        "vice_captains": typing.List[TornEliminationTeamLeader],
                        "captain": None | TornEliminationTeamLeader,
                    },
                ),
            ),
            id=BaseSchema.parse(data.get("id"), EliminationTeamId),
            eliminated_timestamp=BaseSchema.parse(
                data.get("eliminated_timestamp"), None | int
            ),
            eliminated=BaseSchema.parse(data.get("eliminated"), bool),
            attacking_summary=BaseSchema.parse(
                data.get("attacking_summary"),
                typing.List[TornEliminationTeamAttacksSummary],
            ),
        )

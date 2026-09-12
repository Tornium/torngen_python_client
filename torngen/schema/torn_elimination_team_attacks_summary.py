import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .elimination_team_id import EliminationTeamId


@dataclass
class TornEliminationTeamAttacksSummary(BaseSchema):
    """
    JSON object of `TornEliminationTeamAttacksSummary`.
    """

    team_id: EliminationTeamId
    attacks: int

    @staticmethod
    def parse(data):
        return TornEliminationTeamAttacksSummary(
            team_id=BaseSchema.parse(data.get("team_id"), EliminationTeamId),
            attacks=BaseSchema.parse(data.get("attacks"), int),
        )

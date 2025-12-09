import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_elimination_team import TornEliminationTeam


@dataclass
class TornEliminationTeamsResponse(BaseSchema):
    """
    JSON object of `TornEliminationTeamsResponse`.
    """

    elimination: typing.List[TornEliminationTeam]

    @staticmethod
    def parse(data):
        return TornEliminationTeamsResponse(
            elimination=BaseSchema.parse(
                data.get("elimination"), typing.List[TornEliminationTeam]
            ),
        )

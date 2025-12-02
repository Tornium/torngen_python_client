import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_competition_easter_eggs import UserCompetitionEasterEggs
from .user_competition_elimination import UserCompetitionElimination
from .user_competition_halloween import UserCompetitionHalloween
from .user_competition_rps import UserCompetitionRps


@dataclass
class UserCompetitionResponse(BaseSchema):
    """
    JSON object of `UserCompetitionResponse`.
    """

    competition: (
        UserCompetitionElimination
        | UserCompetitionRps
        | UserCompetitionEasterEggs
        | UserCompetitionHalloween
    )

    @staticmethod
    def parse(data):
        return UserCompetitionResponse(
            competition=BaseSchema.parse(
                data.get("competition"),
                UserCompetitionElimination
                | UserCompetitionRps
                | UserCompetitionEasterEggs
                | UserCompetitionHalloween,
            ),
        )

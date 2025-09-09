import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_rps_status import UserRpsStatus


@dataclass
class UserCompetitionRps(BaseSchema):
    """
    JSON object of `UserCompetitionRps`.
    """

    status: UserRpsStatus
    name: typing.Literal["Rock, Paper, Scissors"]
    hp: typing.TypedDict("", {"maximum": int, "current": int})

    @staticmethod
    def parse(data):
        return UserCompetitionRps(
            status=BaseSchema.parse(data.get("status"), UserRpsStatus),
            name=BaseSchema.parse(
                data.get("name"), typing.Literal["Rock, Paper, Scissors"]
            ),
            hp=BaseSchema.parse(
                data.get("hp"), typing.TypedDict("", {"maximum": int, "current": int})
            ),
        )

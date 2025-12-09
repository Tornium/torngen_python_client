import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class TornEliminationTeamPlayer(BaseSchema):
    """
    JSON object of `TornEliminationTeamPlayer`.
    """

    status: UserStatus
    score: int
    name: str
    level: int
    last_action: UserLastAction
    id: UserId
    attacks: int

    @staticmethod
    def parse(data):
        return TornEliminationTeamPlayer(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            score=BaseSchema.parse(data.get("score"), int),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            id=BaseSchema.parse(data.get("id"), UserId),
            attacks=BaseSchema.parse(data.get("attacks"), int),
        )

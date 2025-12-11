import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class TornEliminationTeamLeader(BaseSchema):

    active: bool
    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return TornEliminationTeamLeader(
            active=BaseSchema.parse(data.get("active"), bool),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

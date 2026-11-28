import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .medal_id import MedalId
from .user_medal_progress import UserMedalProgress


@dataclass
class UserMedalDetailed(BaseSchema):
    """
    JSON object of `UserMedalDetailed`.
    """

    timestamp: None | int
    progress: None | UserMedalProgress
    name: str
    is_unlocked: bool
    id: MedalId
    description: str

    @staticmethod
    def parse(data):
        return UserMedalDetailed(
            timestamp=BaseSchema.parse(data.get("timestamp"), None | int),
            progress=BaseSchema.parse(data.get("progress"), None | UserMedalProgress),
            name=BaseSchema.parse(data.get("name"), str),
            is_unlocked=BaseSchema.parse(data.get("is_unlocked"), bool),
            id=BaseSchema.parse(data.get("id"), MedalId),
            description=BaseSchema.parse(data.get("description"), str),
        )

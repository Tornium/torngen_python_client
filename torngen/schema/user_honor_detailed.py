import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .honor_id import HonorId
from .user_honor_progress import UserHonorProgress


@dataclass
class UserHonorDetailed(BaseSchema):
    """
    JSON object of `UserHonorDetailed`.
    """

    timestamp: None | int
    progress: None | UserHonorProgress
    name: str
    is_unlocked: bool
    is_tracked: bool
    id: HonorId
    description: str

    @staticmethod
    def parse(data):
        return UserHonorDetailed(
            timestamp=BaseSchema.parse(data.get("timestamp"), None | int),
            progress=BaseSchema.parse(data.get("progress"), None | UserHonorProgress),
            name=BaseSchema.parse(data.get("name"), str),
            is_unlocked=BaseSchema.parse(data.get("is_unlocked"), bool),
            is_tracked=BaseSchema.parse(data.get("is_tracked"), bool),
            id=BaseSchema.parse(data.get("id"), HonorId),
            description=BaseSchema.parse(data.get("description"), str),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .gym_id import GymId


@dataclass
class UserUnlockedGym(BaseSchema):
    """
    JSON object of `UserUnlockedGym`.
    """

    name: str
    id: GymId
    available: bool

    @staticmethod
    def parse(data):
        return UserUnlockedGym(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), GymId),
            available=BaseSchema.parse(data.get("available"), bool),
        )

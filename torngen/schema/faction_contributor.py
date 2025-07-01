import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionContributor(BaseSchema):
    """
    JSON object of `FactionContributor`.
    """

    value: int
    username: str
    in_faction: bool
    id: UserId

    @staticmethod
    def parse(data):
        return FactionContributor(
            value=BaseSchema.parse(data.get("value"), int),
            username=BaseSchema.parse(data.get("username"), str),
            in_faction=BaseSchema.parse(data.get("in_faction"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

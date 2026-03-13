import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class UserFactionBasic(BaseSchema):
    """
    JSON object of `UserFactionBasic`.
    """

    name: str
    id: FactionId

    @staticmethod
    def parse(data):
        return UserFactionBasic(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
        )

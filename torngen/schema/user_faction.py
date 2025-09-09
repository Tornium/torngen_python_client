import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId


@dataclass
class UserFaction(BaseSchema):
    """
    JSON object of `UserFaction`.
    """

    tag_image: str
    tag: str
    position: str
    name: str
    id: FactionId
    days_in_faction: int

    @staticmethod
    def parse(data):
        return UserFaction(
            tag_image=BaseSchema.parse(data.get("tag_image"), str),
            tag=BaseSchema.parse(data.get("tag"), str),
            position=BaseSchema.parse(data.get("position"), str),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            days_in_faction=BaseSchema.parse(data.get("days_in_faction"), int),
        )

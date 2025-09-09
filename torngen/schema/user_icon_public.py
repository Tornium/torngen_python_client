import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_icon_id import UserIconId


@dataclass
class UserIconPublic(BaseSchema):
    """
    JSON object of `UserIconPublic`.
    """

    title: str
    id: UserIconId
    description: str

    @staticmethod
    def parse(data):
        return UserIconPublic(
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), UserIconId),
            description=BaseSchema.parse(data.get("description"), str),
        )

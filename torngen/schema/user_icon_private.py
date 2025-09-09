import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_icon_id import UserIconId


@dataclass
class UserIconPrivate(BaseSchema):

    until: None | int
    title: str
    id: UserIconId
    description: str

    @staticmethod
    def parse(data):
        return UserIconPrivate(
            until=BaseSchema.parse(data.get("until"), None | int),
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), UserIconId),
            description=BaseSchema.parse(data.get("description"), str),
        )

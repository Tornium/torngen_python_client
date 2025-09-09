import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_icon_private import UserIconPrivate
from .user_icon_public import UserIconPublic


@dataclass
class UserIconsResponse(BaseSchema):
    """
    JSON object of `UserIconsResponse`.
    """

    icons: typing.List[UserIconPublic] | typing.List[UserIconPrivate]

    @staticmethod
    def parse(data):
        return UserIconsResponse(
            icons=BaseSchema.parse(
                data.get("icons"),
                typing.List[UserIconPublic] | typing.List[UserIconPrivate],
            ),
        )

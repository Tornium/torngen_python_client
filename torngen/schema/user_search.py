import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_icon_public import UserIconPublic
from .user_id import UserId
from .user_last_action_status_enum import UserLastActionStatusEnum


@dataclass
class UserSearch(BaseSchema):
    """
    JSON object of `UserSearch`.
    """

    online: UserLastActionStatusEnum
    name: str
    level: int
    id: UserId
    icons: typing.List[UserIconPublic]
    faction_id: FactionId

    @staticmethod
    def parse(data):
        return UserSearch(
            online=BaseSchema.parse(data.get("online"), UserLastActionStatusEnum),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            icons=BaseSchema.parse(data.get("icons"), typing.List[UserIconPublic]),
            faction_id=BaseSchema.parse(data.get("faction_id"), FactionId),
        )

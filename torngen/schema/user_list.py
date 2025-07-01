import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class UserList(BaseSchema):
    """
    JSON object of `UserList`.
    """

    status: UserStatus
    name: str
    level: int
    last_action: UserLastAction
    id: UserId
    faction_id: None | FactionId

    @staticmethod
    def parse(data):
        return UserList(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            id=BaseSchema.parse(data.get("id"), UserId),
            faction_id=BaseSchema.parse(data.get("faction_id"), None | FactionId),
        )

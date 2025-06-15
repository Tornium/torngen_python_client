import typing

from FactionId import FactionId
from UserId import UserId
from UserLastAction import UserLastAction
from UserStatus import UserStatus

from ..base_schema import BaseSchema


class UserList(BaseSchema):

    status: UserStatus
    name: str
    level: int
    last_action: UserLastAction
    id: UserId
    faction_id: None | FactionId

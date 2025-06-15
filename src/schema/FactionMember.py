import typing

from ReviveSetting import ReviveSetting
from UserId import UserId
from UserLastAction import UserLastAction
from UserStatus import UserStatus

from ..base_schema import BaseSchema


class FactionMember(BaseSchema):

    status: UserStatus
    revive_setting: ReviveSetting
    position: str
    name: str
    level: int
    last_action: UserLastAction
    is_revivable: bool
    is_on_wall: bool
    is_in_oc: bool
    id: UserId
    has_early_discharge: bool
    days_in_faction: int

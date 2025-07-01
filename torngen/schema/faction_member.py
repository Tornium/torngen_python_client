import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .revive_setting import ReviveSetting
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class FactionMember(BaseSchema):
    """
    JSON object of `FactionMember`.
    """

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

    @staticmethod
    def parse(data):
        return FactionMember(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            revive_setting=BaseSchema.parse(data.get("revive_setting"), ReviveSetting),
            position=BaseSchema.parse(data.get("position"), str),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            is_revivable=BaseSchema.parse(data.get("is_revivable"), bool),
            is_on_wall=BaseSchema.parse(data.get("is_on_wall"), bool),
            is_in_oc=BaseSchema.parse(data.get("is_in_oc"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
            has_early_discharge=BaseSchema.parse(data.get("has_early_discharge"), bool),
            days_in_faction=BaseSchema.parse(data.get("days_in_faction"), int),
        )

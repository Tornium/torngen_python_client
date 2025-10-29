import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_last_action_status_enum import UserLastActionStatusEnum


@dataclass
class UserLastAction(BaseSchema):
    """
    JSON object of `UserLastAction`.
    """

    timestamp: int
    status: UserLastActionStatusEnum
    relative: str

    @staticmethod
    def parse(data):
        return UserLastAction(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            status=BaseSchema.parse(data.get("status"), UserLastActionStatusEnum),
            relative=BaseSchema.parse(data.get("relative"), str),
        )

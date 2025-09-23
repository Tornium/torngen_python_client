import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .log_id import LogId
from .user_log_id import UserLogId


@dataclass
class UserLog(BaseSchema):
    """
    JSON object of `UserLog`.
    """

    timestamp: int
    params: typing.Dict[str, typing.Any]
    id: UserLogId
    details: typing.TypedDict("", {"title": str, "id": LogId, "category": str})
    data: typing.Dict[str, typing.Any]

    @staticmethod
    def parse(data):
        return UserLog(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            params=BaseSchema.parse(data.get("params"), typing.Dict[str, typing.Any]),
            id=BaseSchema.parse(data.get("id"), UserLogId),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict("", {"title": str, "id": LogId, "category": str}),
            ),
            data=BaseSchema.parse(data.get("data"), typing.Dict[str, typing.Any]),
        )

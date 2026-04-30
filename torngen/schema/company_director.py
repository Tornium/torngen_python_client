import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class CompanyDirector(BaseSchema):
    """
    JSON object of `CompanyDirector`.
    """

    status: UserStatus
    name: str
    last_action: UserLastAction
    id: UserId

    @staticmethod
    def parse(data):
        return CompanyDirector(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            name=BaseSchema.parse(data.get("name"), str),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

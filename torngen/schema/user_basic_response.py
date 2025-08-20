import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_basic import UserBasic


@dataclass
class UserBasicResponse(BaseSchema):
    """
    JSON object of `UserBasicResponse`.
    """

    profile: UserBasic

    @staticmethod
    def parse(data):
        return UserBasicResponse(
            profile=BaseSchema.parse(data.get("profile"), UserBasic),
        )

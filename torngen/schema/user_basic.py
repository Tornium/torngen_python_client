import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_gender_enum import UserGenderEnum
from .user_id import UserId
from .user_status import UserStatus


@dataclass
class UserBasic(BaseSchema):
    """
    JSON object of `UserBasic`.
    """

    status: UserStatus
    name: str
    level: int
    id: UserId
    gender: UserGenderEnum

    @staticmethod
    def parse(data):
        return UserBasic(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            gender=BaseSchema.parse(data.get("gender"), UserGenderEnum),
        )

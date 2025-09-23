import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId
from .user_marital_status_enum import UserMaritalStatusEnum


@dataclass
class ProfileSpouse(BaseSchema):
    """
    JSON object of `ProfileSpouse`.
    """

    status: UserMaritalStatusEnum
    name: str
    id: UserId
    days_married: typing.Optional[int]

    @staticmethod
    def parse(data):
        return ProfileSpouse(
            status=BaseSchema.parse(data.get("status"), UserMaritalStatusEnum),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
            days_married=BaseSchema.parse(
                data.get("days_married"), typing.Optional[int]
            ),
        )

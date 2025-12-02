import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_plane_image_type_enum import UserPlaneImageTypeEnum
from .user_status_state_enum import UserStatusStateEnum


@dataclass
class UserStatus(BaseSchema):
    """
    JSON object of `UserStatus`.
    """

    until: None | int
    state: str | UserStatusStateEnum
    plane_image_type: typing.Optional[UserPlaneImageTypeEnum]
    details: None | str
    description: str
    color: str

    @staticmethod
    def parse(data):
        return UserStatus(
            until=BaseSchema.parse(data.get("until"), None | int),
            state=BaseSchema.parse(data.get("state"), str | UserStatusStateEnum),
            plane_image_type=BaseSchema.parse(
                data.get("plane_image_type"), typing.Optional[UserPlaneImageTypeEnum]
            ),
            details=BaseSchema.parse(data.get("details"), None | str),
            description=BaseSchema.parse(data.get("description"), str),
            color=BaseSchema.parse(data.get("color"), str),
        )

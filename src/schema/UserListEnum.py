from ..base_schema import BaseSchema


class UserListEnum(BaseSchema):

    values = [
        "Friends",
        "Enemies",
        "Targets",
    ]

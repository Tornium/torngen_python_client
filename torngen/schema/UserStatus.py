import typing

from ..base_schema import BaseSchema


class UserStatus(BaseSchema):

    until: None | int
    state: str
    details: None | str
    description: str

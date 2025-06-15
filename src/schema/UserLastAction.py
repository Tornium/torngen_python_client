import typing

from ..base_schema import BaseSchema


class UserLastAction(BaseSchema):

    timestamp: int
    status: str
    relative: str

import typing

from ..base_schema import BaseSchema


class UserSubcrime(BaseSchema):

    total: int
    success: int
    id: int
    fail: int

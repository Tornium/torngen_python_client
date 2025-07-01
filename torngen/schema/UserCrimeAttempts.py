import typing

from UserSubcrime import UserSubcrime

from ..base_schema import BaseSchema


class UserCrimeAttempts(BaseSchema):

    total: int
    success: int
    subcrimes: typing.List[UserSubcrime]
    fail: int
    critical_fail: int

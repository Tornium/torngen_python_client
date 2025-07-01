import typing

from UserHofStats import UserHofStats

from ..base_schema import BaseSchema


class UserHofResponse(BaseSchema):

    hof: UserHofStats

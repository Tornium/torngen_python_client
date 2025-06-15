import typing

from UserCrime import UserCrime

from ..base_schema import BaseSchema


class UserCrimesResponse(BaseSchema):

    crimes: UserCrime

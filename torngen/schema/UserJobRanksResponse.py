import typing

from UserJobRanks import UserJobRanks

from ..base_schema import BaseSchema


class UserJobRanksResponse(BaseSchema):

    jobranks: UserJobRanks

import typing

from UserId import UserId

from ..base_schema import BaseSchema


class ReportFriendOrFoeUser(BaseSchema):

    name: str
    id: UserId

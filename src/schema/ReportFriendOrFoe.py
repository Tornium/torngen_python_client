import typing

from ReportFriendOrFoeUser import ReportFriendOrFoeUser

from ..base_schema import BaseSchema


class ReportFriendOrFoe(BaseSchema):

    friends: typing.List[ReportFriendOrFoeUser]
    enemies: typing.List[ReportFriendOrFoeUser]

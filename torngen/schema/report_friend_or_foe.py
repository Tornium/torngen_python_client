import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .report_friend_or_foe_user import ReportFriendOrFoeUser


@dataclass
class ReportFriendOrFoe(BaseSchema):
    """
    JSON object of `ReportFriendOrFoe`.
    """

    friends: typing.List[ReportFriendOrFoeUser]
    enemies: typing.List[ReportFriendOrFoeUser]

    @staticmethod
    def parse(data):
        return ReportFriendOrFoe(
            friends=BaseSchema.parse(
                data.get("friends"), typing.List[ReportFriendOrFoeUser]
            ),
            enemies=BaseSchema.parse(
                data.get("enemies"), typing.List[ReportFriendOrFoeUser]
            ),
        )

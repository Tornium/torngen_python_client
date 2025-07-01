import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bounty import Bounty


@dataclass
class UserBountiesResponse(BaseSchema):
    """
    JSON object of `UserBountiesResponse`.
    """

    bounties: typing.List[Bounty]

    @staticmethod
    def parse(data):
        return UserBountiesResponse(
            bounties=BaseSchema.parse(data.get("bounties"), typing.List[Bounty]),
        )

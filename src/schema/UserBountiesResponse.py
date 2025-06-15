import typing

from Bounty import Bounty

from ..base_schema import BaseSchema


class UserBountiesResponse(BaseSchema):

    bounties: typing.List[Bounty]

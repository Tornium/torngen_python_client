import typing

from UserFactionBalance import UserFactionBalance

from ..base_schema import BaseSchema


class UserFactionBalanceResponse(BaseSchema):

    factionBalance: None | UserFactionBalance

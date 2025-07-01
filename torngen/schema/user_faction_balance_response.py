import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_faction_balance import UserFactionBalance


@dataclass
class UserFactionBalanceResponse(BaseSchema):
    """
    JSON object of `UserFactionBalanceResponse`.
    """

    factionBalance: None | UserFactionBalance

    @staticmethod
    def parse(data):
        return UserFactionBalanceResponse(
            factionBalance=BaseSchema.parse(
                data.get("factionBalance"), None | UserFactionBalance
            ),
        )

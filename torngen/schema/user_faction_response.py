import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_faction import UserFaction


@dataclass
class UserFactionResponse(BaseSchema):
    """
    JSON object of `UserFactionResponse`.
    """

    faction: None | UserFaction

    @staticmethod
    def parse(data):
        return UserFactionResponse(
            faction=BaseSchema.parse(data.get("faction"), None | UserFaction),
        )

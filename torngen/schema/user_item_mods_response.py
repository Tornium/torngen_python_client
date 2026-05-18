import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_item_mod import UserItemMod


@dataclass
class UserItemModsResponse(BaseSchema):
    """
    JSON object of `UserItemModsResponse`.
    """

    itemmods: typing.List[UserItemMod]

    @staticmethod
    def parse(data):
        return UserItemModsResponse(
            itemmods=BaseSchema.parse(data.get("itemmods"), typing.List[UserItemMod]),
        )

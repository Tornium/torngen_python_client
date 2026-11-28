import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_display_item import UserDisplayItem


@dataclass
class UserDisplay(BaseSchema):
    """
    JSON object of `UserDisplay`.
    """

    items: typing.List[UserDisplayItem]

    @staticmethod
    def parse(data):
        return UserDisplay(
            items=BaseSchema.parse(data.get("items"), typing.List[UserDisplayItem]),
        )

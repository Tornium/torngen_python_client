import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_bazaar_item import UserBazaarItem


@dataclass
class UserBazaar(BaseSchema):
    """
    JSON object of `UserBazaar`.
    """

    items: typing.List[UserBazaarItem]
    is_open: bool
    exists: bool

    @staticmethod
    def parse(data):
        return UserBazaar(
            items=BaseSchema.parse(data.get("items"), typing.List[UserBazaarItem]),
            is_open=BaseSchema.parse(data.get("is_open"), bool),
            exists=BaseSchema.parse(data.get("exists"), bool),
        )

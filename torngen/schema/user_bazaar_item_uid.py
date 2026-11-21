import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_uid import ItemUid


@dataclass
class UserBazaarItemUid(BaseSchema):
    """
    JSON object of `UserBazaarItemUid`.
    """

    uid: ItemUid
    price: int

    @staticmethod
    def parse(data):
        return UserBazaarItemUid(
            uid=BaseSchema.parse(data.get("uid"), ItemUid),
            price=BaseSchema.parse(data.get("price"), int),
        )

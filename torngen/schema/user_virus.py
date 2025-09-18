import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class UserVirus(BaseSchema):
    """
    JSON object of `UserVirus`.
    """

    until: int
    item: typing.TypedDict("", {"name": str, "id": ItemId})

    @staticmethod
    def parse(data):
        return UserVirus(
            until=BaseSchema.parse(data.get("until"), int),
            item=BaseSchema.parse(
                data.get("item"), typing.TypedDict("", {"name": str, "id": ItemId})
            ),
        )

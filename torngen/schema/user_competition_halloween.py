import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class UserCompetitionHalloween(BaseSchema):
    """
    JSON object of `UserCompetitionHalloween`.
    """

    treats_collected: int
    name: typing.Literal["Halloween"]
    basket: typing.TypedDict("", {"name": str, "id": ItemId})

    @staticmethod
    def parse(data):
        return UserCompetitionHalloween(
            treats_collected=BaseSchema.parse(data.get("treats_collected"), int),
            name=BaseSchema.parse(data.get("name"), typing.Literal["Halloween"]),
            basket=BaseSchema.parse(
                data.get("basket"), typing.TypedDict("", {"name": str, "id": ItemId})
            ),
        )

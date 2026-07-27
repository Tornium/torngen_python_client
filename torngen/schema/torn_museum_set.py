import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_id import ItemId


@dataclass
class TornMuseumSet(BaseSchema):
    """
    JSON object of `TornMuseumSet`.
    """

    points: int
    name: str
    items: typing.List[ItemId]

    @staticmethod
    def parse(data):
        return TornMuseumSet(
            points=BaseSchema.parse(data.get("points"), int),
            name=BaseSchema.parse(data.get("name"), str),
            items=BaseSchema.parse(data.get("items"), typing.List[ItemId]),
        )

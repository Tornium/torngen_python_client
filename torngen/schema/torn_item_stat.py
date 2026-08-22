import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_stat_id import ItemStatId


@dataclass
class TornItemStat(BaseSchema):
    """
    JSON object of `TornItemStat`.
    """

    value: int
    title: str
    id: ItemStatId

    @staticmethod
    def parse(data):
        return TornItemStat(
            value=BaseSchema.parse(data.get("value"), int),
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), ItemStatId),
        )

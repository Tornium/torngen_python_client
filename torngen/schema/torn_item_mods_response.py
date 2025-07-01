import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_item_mods import TornItemMods


@dataclass
class TornItemModsResponse(BaseSchema):
    """
    JSON object of `TornItemModsResponse`.
    """

    itemmods: typing.List[TornItemMods]

    @staticmethod
    def parse(data):
        return TornItemModsResponse(
            itemmods=BaseSchema.parse(data.get("itemmods"), typing.List[TornItemMods]),
        )

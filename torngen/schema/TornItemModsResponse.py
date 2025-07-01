import typing

from TornItemMods import TornItemMods

from ..base_schema import BaseSchema


class TornItemModsResponse(BaseSchema):

    itemmods: typing.List[TornItemMods]

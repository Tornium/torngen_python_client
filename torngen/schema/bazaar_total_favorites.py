import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarTotalFavorites(BaseSchema):
    value: typing.List[typing.TypedDict("", {"total_favorites": int}) | Bazaar]

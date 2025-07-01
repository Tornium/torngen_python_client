import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarRecentFavorites(BaseSchema):
    value: typing.List[typing.TypedDict("", {"recent_favorites": int}) | Bazaar]

import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarRecentFavorites(BaseSchema):
    value: typing.List[typing.TypedDict("", {"recent_favorites": int}) | Bazaar]

import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarTotalFavorites(BaseSchema):
    value: typing.List[typing.TypedDict("", {"total_favorites": int}) | Bazaar]

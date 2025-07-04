import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class BazaarRecentFavorites(BaseSchema):

    recent_favorites: int
    name: str
    is_open: bool
    id: UserId

    @staticmethod
    def parse(data):
        return BazaarRecentFavorites(
            recent_favorites=BaseSchema.parse(data.get("recent_favorites"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_open=BaseSchema.parse(data.get("is_open"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

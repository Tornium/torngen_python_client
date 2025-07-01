import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class BasicUser(BaseSchema):
    """
    JSON object of `BasicUser`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return BasicUser(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

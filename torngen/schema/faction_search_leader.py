import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionSearchLeader(BaseSchema):
    """
    JSON object of `FactionSearchLeader`.
    """

    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return FactionSearchLeader(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .merit_id import MeritId


@dataclass
class TornMerit(BaseSchema):
    """
    JSON object of `TornMerit`.
    """

    name: str
    id: MeritId
    description: str

    @staticmethod
    def parse(data):
        return TornMerit(
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), MeritId),
            description=BaseSchema.parse(data.get("description"), str),
        )

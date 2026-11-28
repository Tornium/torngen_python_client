import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornRankedWarTemplateEntry(BaseSchema):
    """
    JSON object of `TornRankedWarTemplateEntry`.
    """

    name: str
    description: None | str

    @staticmethod
    def parse(data):
        return TornRankedWarTemplateEntry(
            name=BaseSchema.parse(data.get("name"), str),
            description=BaseSchema.parse(data.get("description"), None | str),
        )

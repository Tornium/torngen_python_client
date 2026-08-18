import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornCard(BaseSchema):
    """
    JSON object of `TornCard`.
    """

    short_name: str
    name: str
    class_: str

    @staticmethod
    def parse(data):
        return TornCard(
            short_name=BaseSchema.parse(data.get("short_name"), str),
            name=BaseSchema.parse(data.get("name"), str),
            class_=BaseSchema.parse(data.get("class"), str),
        )

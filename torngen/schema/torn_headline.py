import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornHeadline(BaseSchema):
    """
    JSON object of `TornHeadline`.
    """

    type: str
    link: None | str
    importance: typing.Literal["normal", "urgent"]
    id: None | int
    headline: str

    @staticmethod
    def parse(data):
        return TornHeadline(
            type=BaseSchema.parse(data.get("type"), str),
            link=BaseSchema.parse(data.get("link"), None | str),
            importance=BaseSchema.parse(
                data.get("importance"), typing.Literal["normal", "urgent"]
            ),
            id=BaseSchema.parse(data.get("id"), None | int),
            headline=BaseSchema.parse(data.get("headline"), str),
        )

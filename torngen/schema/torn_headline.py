import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornHeadline(BaseSchema):
    """
    JSON object of `TornHeadline`.
    """

    type: str
    start_at: int
    link: None | str
    importance: typing.Literal["normal", "urgent"]
    id: None | int
    headline: str
    has_countdown: bool
    end_at: int

    @staticmethod
    def parse(data):
        return TornHeadline(
            type=BaseSchema.parse(data.get("type"), str),
            start_at=BaseSchema.parse(data.get("start_at"), int),
            link=BaseSchema.parse(data.get("link"), None | str),
            importance=BaseSchema.parse(
                data.get("importance"), typing.Literal["normal", "urgent"]
            ),
            id=BaseSchema.parse(data.get("id"), None | int),
            headline=BaseSchema.parse(data.get("headline"), str),
            has_countdown=BaseSchema.parse(data.get("has_countdown"), bool),
            end_at=BaseSchema.parse(data.get("end_at"), int),
        )

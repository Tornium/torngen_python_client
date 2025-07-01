import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_thread_extended import ForumThreadExtended


@dataclass
class ForumThreadResponse(BaseSchema):
    """
    JSON object of `ForumThreadResponse`.
    """

    thread: ForumThreadExtended

    @staticmethod
    def parse(data):
        return ForumThreadResponse(
            thread=BaseSchema.parse(data.get("thread"), ForumThreadExtended),
        )

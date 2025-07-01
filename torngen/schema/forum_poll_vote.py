import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ForumPollVote(BaseSchema):
    """
    JSON object of `ForumPollVote`.
    """

    votes: int
    answer: str

    @staticmethod
    def parse(data):
        return ForumPollVote(
            votes=BaseSchema.parse(data.get("votes"), int),
            answer=BaseSchema.parse(data.get("answer"), str),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_poll_vote import ForumPollVote


@dataclass
class ForumPoll(BaseSchema):
    """
    JSON object of `ForumPoll`.
    """

    question: str
    answers_count: int
    answers: typing.List[ForumPollVote]

    @staticmethod
    def parse(data):
        return ForumPoll(
            question=BaseSchema.parse(data.get("question"), str),
            answers_count=BaseSchema.parse(data.get("answers_count"), int),
            answers=BaseSchema.parse(data.get("answers"), typing.List[ForumPollVote]),
        )

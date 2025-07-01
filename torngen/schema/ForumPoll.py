import typing

from ForumPollVote import ForumPollVote

from ..base_schema import BaseSchema


class ForumPoll(BaseSchema):

    question: str
    answers_count: int
    answers: typing.List[ForumPollVote]

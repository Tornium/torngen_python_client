import typing

from ..base_schema import BaseSchema


class ForumPollVote(BaseSchema):

    votes: int
    answer: str

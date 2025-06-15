import typing

from ..base_schema import BaseSchema


class ForumSubscribedThreadPostsCount(BaseSchema):

    total: int
    new: int

import typing

from UserId import UserId

from ..base_schema import BaseSchema


class ForumThreadAuthor(BaseSchema):

    username: str
    karma: int
    id: UserId

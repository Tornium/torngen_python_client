import typing

from ForumId import ForumId

from ..base_schema import BaseSchema


class ForumCategoriesResponse(BaseSchema):

    categories: typing.List[
        typing.TypedDict(
            "", {"title": str, "threads": int, "id": ForumId, "acronym": str}
        )
    ]

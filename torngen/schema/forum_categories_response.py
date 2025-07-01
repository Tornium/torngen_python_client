import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .forum_id import ForumId


@dataclass
class ForumCategoriesResponse(BaseSchema):
    """
    JSON object of `ForumCategoriesResponse`.
    """

    categories: typing.List[
        typing.TypedDict(
            "", {"title": str, "threads": int, "id": ForumId, "acronym": str}
        )
    ]

    @staticmethod
    def parse(data):
        return ForumCategoriesResponse(
            categories=BaseSchema.parse(
                data.get("categories"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {"title": str, "threads": int, "id": ForumId, "acronym": str},
                    )
                ],
            ),
        )

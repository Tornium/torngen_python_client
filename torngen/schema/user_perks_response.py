import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserPerksResponse(BaseSchema):
    """
    JSON object of `UserPerksResponse`.
    """

    perks: typing.TypedDict(
        "",
        {
            "stock": typing.List[str],
            "property": typing.List[str],
            "merit": typing.List[str],
            "job": typing.List[str],
            "faction": typing.List[str],
            "enhancer": typing.List[str],
            "education": typing.List[str],
            "book": typing.List[str],
        },
    )

    @staticmethod
    def parse(data):
        return UserPerksResponse(
            perks=BaseSchema.parse(
                data.get("perks"),
                typing.TypedDict(
                    "",
                    {
                        "stock": typing.List[str],
                        "property": typing.List[str],
                        "merit": typing.List[str],
                        "job": typing.List[str],
                        "faction": typing.List[str],
                        "enhancer": typing.List[str],
                        "education": typing.List[str],
                        "book": typing.List[str],
                    },
                ),
            ),
        )

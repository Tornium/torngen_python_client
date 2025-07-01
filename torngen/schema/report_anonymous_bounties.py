import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class ReportAnonymousBounties(BaseSchema):
    """
    JSON object of `ReportAnonymousBounties`.
    """

    bounties: typing.List[
        typing.TypedDict(
            "",
            {
                "user": None | typing.TypedDict("", {"name": str, "id": UserId}),
                "text": str,
                "bounty": int,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return ReportAnonymousBounties(
            bounties=BaseSchema.parse(
                data.get("bounties"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "user": None
                            | typing.TypedDict("", {"name": str, "id": UserId}),
                            "text": str,
                            "bounty": int,
                        },
                    )
                ],
            ),
        )

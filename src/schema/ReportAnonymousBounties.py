import typing

from UserId import UserId

from ..base_schema import BaseSchema


class ReportAnonymousBounties(BaseSchema):

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

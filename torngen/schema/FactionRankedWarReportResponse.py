import typing

from FactionId import FactionId
from ItemId import ItemId
from RankedWarId import RankedWarId
from UserId import UserId

from ..base_schema import BaseSchema


class FactionRankedWarReportResponse(BaseSchema):

    rankedwarreport: typing.TypedDict(
        "",
        {
            "winner": FactionId,
            "start": int,
            "id": RankedWarId,
            "forfeit": bool,
            "factions": typing.List[
                typing.TypedDict(
                    "",
                    {
                        "score": int,
                        "rewards": typing.TypedDict(
                            "",
                            {
                                "respect": int,
                                "points": int,
                                "items": typing.List[
                                    typing.TypedDict(
                                        "", {"quantity": int, "name": str, "id": ItemId}
                                    )
                                ],
                            },
                        ),
                        "rank": typing.TypedDict("", {"before": str, "after": str}),
                        "name": str,
                        "members": typing.List[
                            typing.TypedDict(
                                "",
                                {
                                    "score": int | float,
                                    "name": str,
                                    "level": int,
                                    "id": UserId,
                                    "attacks": int,
                                },
                            )
                        ],
                        "id": FactionId,
                        "attacks": int,
                    },
                )
            ],
            "end": int,
        },
    )

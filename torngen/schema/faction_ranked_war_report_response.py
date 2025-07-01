import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .item_id import ItemId
from .ranked_war_id import RankedWarId
from .user_id import UserId


@dataclass
class FactionRankedWarReportResponse(BaseSchema):
    """
    JSON object of `FactionRankedWarReportResponse`.
    """

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

    @staticmethod
    def parse(data):
        return FactionRankedWarReportResponse(
            rankedwarreport=BaseSchema.parse(
                data.get("rankedwarreport"),
                typing.TypedDict(
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
                                                    "",
                                                    {
                                                        "quantity": int,
                                                        "name": str,
                                                        "id": ItemId,
                                                    },
                                                )
                                            ],
                                        },
                                    ),
                                    "rank": typing.TypedDict(
                                        "", {"before": str, "after": str}
                                    ),
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
                ),
            ),
        )

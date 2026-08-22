import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class TornRockPaperScissorsResponse(BaseSchema):
    """
    JSON object of `TornRockPaperScissorsResponse`.
    """

    rockpaperscissors: typing.List[
        typing.TypedDict(
            "", {"type": typing.Literal["rock", "paper", "scissors"], "count": int}
        )
    ]

    @staticmethod
    def parse(data):
        return TornRockPaperScissorsResponse(
            rockpaperscissors=BaseSchema.parse(
                data.get("rockpaperscissors"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "type": typing.Literal["rock", "paper", "scissors"],
                            "count": int,
                        },
                    )
                ],
            ),
        )

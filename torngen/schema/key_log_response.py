import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class KeyLogResponse(BaseSchema):
    """
    JSON object of `KeyLogResponse`.
    """

    log: typing.List[
        typing.TypedDict(
            "",
            {
                "type": str,
                "timestamp": int,
                "selections": str,
                "ip": str,
                "id": None | str | int,
                "comment": None | str,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return KeyLogResponse(
            log=BaseSchema.parse(
                data.get("log"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "type": str,
                            "timestamp": int,
                            "selections": str,
                            "ip": str,
                            "id": None | str | int,
                            "comment": None | str,
                        },
                    )
                ],
            ),
        )

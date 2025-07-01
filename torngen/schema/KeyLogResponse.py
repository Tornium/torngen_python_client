import typing

from ..base_schema import BaseSchema


class KeyLogResponse(BaseSchema):

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

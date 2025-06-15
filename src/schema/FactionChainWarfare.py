import typing

from FactionChain import FactionChain
from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionChainWarfare(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "", {"faction": typing.TypedDict("", {"name": str, "id": FactionId})}
        )
        | FactionChain
    ]

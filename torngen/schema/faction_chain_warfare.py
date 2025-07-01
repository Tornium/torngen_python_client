import typing

from ..base_schema import BaseSchema
from .faction_chain import FactionChain
from .faction_id import FactionId


class FactionChainWarfare(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "", {"faction": typing.TypedDict("", {"name": str, "id": FactionId})}
        )
        | FactionChain
    ]

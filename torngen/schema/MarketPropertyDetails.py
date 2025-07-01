import typing

from BasicProperty import BasicProperty
from PropertyModificationEnum import PropertyModificationEnum

from ..base_schema import BaseSchema


class MarketPropertyDetails(BaseSchema):

    property: BasicProperty
    listings: typing.List[
        typing.TypedDict(
            "",
            {
                "upkeep": int,
                "modifications": typing.List[PropertyModificationEnum],
                "market_price": int,
                "happy": int,
                "cost": int,
            },
        )
    ]

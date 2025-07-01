import typing

from BasicProperty import BasicProperty
from PropertyModificationEnum import PropertyModificationEnum

from ..base_schema import BaseSchema


class MarketRentalDetails(BaseSchema):

    property: BasicProperty
    listings: typing.List[
        typing.TypedDict(
            "",
            {
                "upkeep": int,
                "rental_period": int,
                "modifications": typing.List[PropertyModificationEnum],
                "market_price": int,
                "happy": int,
                "cost_per_day": int,
                "cost": int,
            },
        )
    ]

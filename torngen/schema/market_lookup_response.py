import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_selection_name import MarketSelectionName


@dataclass
class MarketLookupResponse(BaseSchema):
    """
    JSON object of `MarketLookupResponse`.
    """

    selections: typing.List[MarketSelectionName]

    @staticmethod
    def parse(data):
        return MarketLookupResponse(
            selections=BaseSchema.parse(
                data.get("selections"), typing.List[MarketSelectionName]
            ),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .item_market import ItemMarket
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal


@dataclass
class MarketItemMarketResponse(BaseSchema):
    """
    JSON object of `MarketItemMarketResponse`.
    """

    itemmarket: ItemMarket
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return MarketItemMarketResponse(
            itemmarket=BaseSchema.parse(data.get("itemmarket"), ItemMarket),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

import typing

from ItemMarket import ItemMarket
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class MarketItemMarketResponse(BaseSchema):

    itemmarket: ItemMarket
    _metadata: RequestMetadataWithLinks

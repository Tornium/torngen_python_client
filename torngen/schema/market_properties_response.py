import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_property_details import MarketPropertyDetails
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class MarketPropertiesResponse(BaseSchema):
    """
    JSON object of `MarketPropertiesResponse`.
    """

    properties: MarketPropertyDetails
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return MarketPropertiesResponse(
            properties=BaseSchema.parse(data.get("properties"), MarketPropertyDetails),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

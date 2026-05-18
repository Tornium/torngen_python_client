import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_property_details import MarketPropertyDetails
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal


@dataclass
class MarketPropertiesResponse(BaseSchema):
    """
    JSON object of `MarketPropertiesResponse`.
    """

    properties_timestamp: int
    properties_delay: typing.Optional[int]
    properties: MarketPropertyDetails
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return MarketPropertiesResponse(
            properties_timestamp=BaseSchema.parse(
                data.get("properties_timestamp"), int
            ),
            properties_delay=BaseSchema.parse(
                data.get("properties_delay"), typing.Optional[int]
            ),
            properties=BaseSchema.parse(data.get("properties"), MarketPropertyDetails),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

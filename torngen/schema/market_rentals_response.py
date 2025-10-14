import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_rental_details import MarketRentalDetails
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class MarketRentalsResponse(BaseSchema):
    """
    JSON object of `MarketRentalsResponse`.
    """

    rentals: MarketRentalDetails
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return MarketRentalsResponse(
            rentals=BaseSchema.parse(data.get("rentals"), MarketRentalDetails),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

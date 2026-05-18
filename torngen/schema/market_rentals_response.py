import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .market_rental_details import MarketRentalDetails
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal


@dataclass
class MarketRentalsResponse(BaseSchema):
    """
    JSON object of `MarketRentalsResponse`.
    """

    rentals_timestamp: int
    rentals_delay: typing.Optional[int]
    rentals: MarketRentalDetails
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return MarketRentalsResponse(
            rentals_timestamp=BaseSchema.parse(data.get("rentals_timestamp"), int),
            rentals_delay=BaseSchema.parse(
                data.get("rentals_delay"), typing.Optional[int]
            ),
            rentals=BaseSchema.parse(data.get("rentals"), MarketRentalDetails),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

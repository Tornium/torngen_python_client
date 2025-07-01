import typing

from MarketRentalDetails import MarketRentalDetails
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class MarketRentalsResponse(BaseSchema):

    properties: MarketRentalDetails
    _metadata: RequestMetadataWithLinks

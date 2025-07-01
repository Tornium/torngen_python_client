import typing

from MarketPropertyDetails import MarketPropertyDetails
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class MarketPropertiesResponse(BaseSchema):

    properties: MarketPropertyDetails
    _metadata: RequestMetadataWithLinks

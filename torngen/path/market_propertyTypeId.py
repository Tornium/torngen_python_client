from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.market_properties_response import MarketPropertiesResponse
from ..schema.market_rentals_response import MarketRentalsResponse


class MarketPropertyTypeId(BaseQuery):
    """
    A collection of paths representing `MarketPropertyTypeId`.
    """

    properties = Path(
        "/market/{propertyTypeId}/properties",
        MarketPropertiesResponse,
        propertyTypeId=Parameter(
            "propertyTypeId", "path", required=True, deprecated=False
        ),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{propertyTypeId}/properties`: Get properties market listings
    Requires public access key.

    # Parameters
    - propertyTypeId : Property type id
    - offset : N/A
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    rentals = Path(
        "/market/{propertyTypeId}/rentals",
        MarketRentalsResponse,
        propertyTypeId=Parameter(
            "propertyTypeId", "path", required=True, deprecated=False
        ),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{propertyTypeId}/rentals`: Get properties rental listings
    Requires public access key.

    # Parameters
    - propertyTypeId : Property type id
    - offset : N/A
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="market/{propertyTypeId}")

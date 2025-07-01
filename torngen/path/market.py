from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.bazaar_response import BazaarResponse
from ..schema.market_lookup_response import MarketLookupResponse
from ..schema.timestamp_response import TimestampResponse


class Market(BaseQuery):
    """
    A collection of paths representing `Market`.

    Paths
    -----
    - `/market/bazaar` : Get bazaar directory
    - `/market/lookup` : Get all available market selections
    - `/market/timestamp` : Get current server time


    `/market/bazaar`
    -------------
    Get bazaar directory
    Requires public access key. <br> The default response is of type 'BazaarWeekly', but if a category is chosen, the response will be of type 'BazaarSpecialized'.

    # Parameters
    - cat : Category of specialized bazaars returned
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/market/lookup`
    -------------
    Get all available market selections
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/market/timestamp`
    -------------
    Get current server time
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    bazaar = Path(
        "/market/bazaar",
        BazaarResponse,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/market/lookup",
        MarketLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/market/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="market")

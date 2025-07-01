from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.bazaar_response_specialized import BazaarResponseSpecialized
from ..schema.market_item_market_response import MarketItemMarketResponse


class MarketId(BaseQuery):
    """
    A collection of paths representing `MarketId`.

    Paths
    -----
    - `/market/{id}/itemmarket` : Get item market listings
    - `/market/{id}/bazaar` : Get item specialized bazaar directory


    `/market/{id}/itemmarket`
    -------------
    Get item market listings
    Requires public access key. <br>

    # Parameters
    - id : Item id
    - bonus : Used to filter weapons with a specific bonus.
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/market/{id}/bazaar`
    -------------
    Get item specialized bazaar directory
    Requires public access key. <br>

    # Parameters
    - id : Item id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    itemmarket = Path(
        "/market/{id}/itemmarket",
        MarketItemMarketResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        bonus=Parameter("bonus", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    bazaar = Path(
        "/market/{id}/bazaar",
        BazaarResponseSpecialized,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="market_id")

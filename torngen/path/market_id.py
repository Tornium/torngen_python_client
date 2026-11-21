from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.auction_house_listing_response import AuctionHouseListingResponse
from ..schema.auction_house_response import AuctionHouseResponse
from ..schema.bazaar_response_specialized import BazaarResponseSpecialized
from ..schema.market_item_market_response import MarketItemMarketResponse


class MarketId(BaseQuery):
    """
    A collection of paths representing `MarketId`.
    """

    itemmarket = Path(
        "/market/{id}/itemmarket",
        MarketItemMarketResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        bonus=Parameter("bonus", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{id}/itemmarket`: Get item market listings
    <b>Globally cached selection (1 hour).</b> Requires public access key.

    # Parameters
    - id : Item id
    - bonus : Used to filter weapons with a specific bonus.
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    bazaar = Path(
        "/market/{id}/bazaar",
        BazaarResponseSpecialized,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{id}/bazaar`: Get item specialized bazaar directory
    Requires public access key.

    # Parameters
    - id : Item id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    auctionhouselisting = Path(
        "/market/{id}/auctionhouselisting",
        AuctionHouseListingResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{id}/auctionhouselisting`: Get specific item auction house listings
    <b>Globally cached selection (15 minutes, ongoing listings only).</b> Requires public access key. Ongoing listings are returned from the cached and delayed ongoing listings.

    # Parameters
    - id : Listing id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    auctionhouse = Path(
        "/market/{id}/auctionhouse",
        AuctionHouseResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/{id}/auctionhouse`: Get specific item auction house listings
    <b>Globally cached selection (15 minutes, ongoing listings only).</b> Requires public access key. Ongoing listings are cached and delayed; auctionhouse_timestamp and auctionhouse_delay are returned only for the ongoing category. Listings are sorted by their end time: complete listings descending by default, ongoing listings ascending by default.

    # Parameters
    - id : Item id
    - cat : Listings category, defaults to complete
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="market/{id}")

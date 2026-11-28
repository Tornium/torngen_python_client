from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.auction_house_response import AuctionHouseResponse
from ..schema.bazaar_response import BazaarResponse
from ..schema.market_lookup_response import MarketLookupResponse
from ..schema.market_points_history_response import MarketPointsHistoryResponse
from ..schema.points_market_response import PointsMarketResponse
from ..schema.timestamp_response import TimestampResponse


class Market(BaseQuery):
    """
    A collection of paths representing `Market`.
    """

    bazaar = Path(
        "/market/bazaar",
        BazaarResponse,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/bazaar`: Get bazaar directory
    Requires public access key. The default response is of type 'BazaarWeekly', but if a category is chosen, the response will be of type 'BazaarSpecialized'.

    # Parameters
    - cat : Category of specialized bazaars returned
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    auctionhouse = Path(
        "/market/auctionhouse",
        AuctionHouseResponse,
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
    `/market/auctionhouse`: Get auction house listings
    <b>Globally cached selection (15 minutes, ongoing listings only).</b> Requires public access key. Ongoing listings are cached and delayed; auctionhouse_timestamp and auctionhouse_delay are returned only for the ongoing category. Listings are sorted by their end time: complete listings descending by default, ongoing listings ascending by default.

    # Parameters
    - cat : Listings category, defaults to complete
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    lookup = Path(
        "/market/lookup",
        MarketLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/lookup`: Get all available market selections
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    pointshistory = Path(
        "/market/pointshistory",
        MarketPointsHistoryResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/pointshistory`: Get points price and circulation history
    Requires public access key. Returns the daily average points market price and the total points in circulation, one entry per day, as used for the points price graph.

    # Parameters
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    timestamp = Path(
        "/market/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/timestamp`: Get current server time
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    pointsmarket = Path(
        "/market/pointsmarket",
        PointsMarketResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/market/pointsmarket`: Get points market listings
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="market")

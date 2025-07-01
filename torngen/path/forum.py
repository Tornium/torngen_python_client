from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.forum_categories_response import ForumCategoriesResponse
from ..schema.forum_lookup_response import ForumLookupResponse
from ..schema.forum_threads_response import ForumThreadsResponse
from ..schema.timestamp_response import TimestampResponse


class Forum(BaseQuery):
    """
    A collection of paths representing `Forum`.

    Paths
    -----
    - `/forum/lookup` : Get all available forum selections
    - `/forum/threads` : Get threads across all forum categories
    - `/forum/timestamp` : Get current server time
    - `/forum/categories` : Get publicly available forum categories


    `/forum/lookup`
    -------------
    Get all available forum selections
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/forum/threads`
    -------------
    Get threads across all forum categories
    Requires public access key. <br>

    # Parameters
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/forum/timestamp`
    -------------
    Get current server time
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/forum/categories`
    -------------
    Get publicly available forum categories
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    lookup = Path(
        "/forum/lookup",
        ForumLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    threads = Path(
        "/forum/threads",
        ForumThreadsResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/forum/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    categories = Path(
        "/forum/categories",
        ForumCategoriesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="forum")

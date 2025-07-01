from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.forum_threads_response import ForumThreadsResponse


class ForumCategoryIds(BaseQuery):
    """
    A collection of paths representing `ForumCategoryIds`.

    Paths
    -----
    - `/forum/{categoryIds}/threads` : Get threads for specific public forum category or categories


    `/forum/{categoryIds}/threads`
    -------------
    Get threads for specific public forum category or categories
    Requires public access key. <br>

    # Parameters
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - categoryIds : Category id or a list of category ids (comma separated)
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    threads = Path(
        "/forum/{categoryIds}/threads",
        ForumThreadsResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        categoryIds=Parameter("categoryIds", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="forum_categoryIds")

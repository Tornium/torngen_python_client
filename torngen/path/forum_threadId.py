from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class ForumThreadId(BaseQuery):
    """
    A collection of paths representing `ForumThreadId`.

    Paths
    -----
    - `/forum/{threadId}/thread` : Get specific thread details
    - `/forum/{threadId}/posts` : Get specific forum thread posts


    `/forum/{threadId}/thread`
    -------------
    Get specific thread details
    Requires public access key. <br>Contains details of a thread including topic content and poll (if any).

    # Parameters
    - threadId : Thread id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/forum/{threadId}/posts`
    -------------
    Get specific forum thread posts
    Requires public access key. <br>Returns 20 posts per page for a specific thread.

    # Parameters
    - offset : N/A
    - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
    - threadId : Thread id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    thread = Path(
        "/forum/{threadId}/thread",
        None,
        threadId=Parameter("threadId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    posts = Path(
        "/forum/{threadId}/posts",
        None,
        offset=Parameter("offset", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        threadId=Parameter("threadId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

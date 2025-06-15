from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class ForumThreadId(BaseQuery):
    """
    A collection of paths representing `ForumThreadId`.

    Paths
    -----
    /forum/{threadId}/thread : Get specific thread details
    /forum/{threadId}/posts : Get specific forum thread posts
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

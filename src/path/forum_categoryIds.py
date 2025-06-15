from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class ForumCategoryIds(BaseQuery):
    """
    A collection of paths representing `ForumCategoryIds`.

    Paths
    -----
    /forum/{categoryIds}/threads : Get threads for specific public forum category or categories
    """

    threads = Path(
        "/forum/{categoryIds}/threads",
        None,
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
        super().__init__()

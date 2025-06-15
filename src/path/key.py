from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Key(BaseQuery):
    """
    A collection of paths representing `Key`.

    Paths
    -----
    /key/info : Get current key info
    /key/log : Get current key log history
    """

    info = Path(
        "/key/info",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    log = Path(
        "/key/log",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class TornIds(BaseQuery):
    """
    A collection of paths representing `TornIds`.

    Paths
    -----
    /torn/{ids}/items : Get information about items
    """

    items = Path(
        "/torn/{ids}/items",
        None,
        ids=Parameter("ids", "path", required=True, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

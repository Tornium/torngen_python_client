from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class TornLogCategoryId(BaseQuery):
    """
    A collection of paths representing `TornLogCategoryId`.

    Paths
    -----
    /torn/{logCategoryId}/logtypes : Get available log ids for a specific log category
    """

    logtypes = Path(
        "/torn/{logCategoryId}/logtypes",
        None,
        logCategoryId=Parameter(
            "logCategoryId", "path", required=True, deprecated=False
        ),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

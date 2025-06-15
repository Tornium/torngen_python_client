from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class MarketId(BaseQuery):
    """
    A collection of paths representing `MarketId`.

    Paths
    -----
    /market/{id}/itemmarket : Get item market listings
    /market/{id}/bazaar : Get item specialized bazaar directory
    """

    itemmarket = Path(
        "/market/{id}/itemmarket",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        bonus=Parameter("bonus", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    bazaar = Path(
        "/market/{id}/bazaar",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Racing(BaseQuery):
    """
    A collection of paths representing `Racing`.

    Paths
    -----
    /racing/tracks : Get race tracks and descriptions
    /racing/timestamp : Get current server time
    /racing/carupgrades : Get all possible car upgrades
    /racing/lookup : Get all available racing selections
    /racing/cars : Get cars and their racing stats
    /racing/races : Get races
    """

    tracks = Path(
        "/racing/tracks",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/racing/timestamp",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    carupgrades = Path(
        "/racing/carupgrades",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/racing/lookup",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    cars = Path(
        "/racing/cars",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    races = Path(
        "/racing/races",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

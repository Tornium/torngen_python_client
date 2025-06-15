from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class FactionCrimeId(BaseQuery):
    """
    A collection of paths representing `FactionCrimeId`.

    Paths
    -----
    /faction/{crimeId}/crime : Get a specific organized crime
    """

    crime = Path(
        "/faction/{crimeId}/crime",
        None,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

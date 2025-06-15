from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class UserCrimeId(BaseQuery):
    """
    A collection of paths representing `UserCrimeId`.

    Paths
    -----
    /user/{crimeId}/crimes : Get your crime statistics
    """

    crimes = Path(
        "/user/{crimeId}/crimes",
        None,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

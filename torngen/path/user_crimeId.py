from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class UserCrimeId(BaseQuery):
    """
    A collection of paths representing `UserCrimeId`.

    Paths
    -----
    - `/user/{crimeId}/crimes` : Get your crime statistics


    `/user/{crimeId}/crimes`
    -------------
    Get your crime statistics
    Requires minimal access key. <br>Return the details and statistics about for a specific crime.

    # Parameters
    - crimeId : Crime id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

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

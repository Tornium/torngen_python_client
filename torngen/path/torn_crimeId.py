from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.torn_subcrimes_response import TornSubcrimesResponse


class TornCrimeId(BaseQuery):
    """
    A collection of paths representing `TornCrimeId`.

    Paths
    -----
    - `/torn/{crimeId}/subcrimes` : Get Subcrimes information


    `/torn/{crimeId}/subcrimes`
    -------------
    Get Subcrimes information
    Requires public access key. <br> Return the details about possible actions for a specific crime.

    # Parameters
    - crimeId : Crime id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    subcrimes = Path(
        "/torn/{crimeId}/subcrimes",
        TornSubcrimesResponse,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="torn/{crimeId}")

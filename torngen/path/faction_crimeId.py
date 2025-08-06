from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_crime_response import FactionCrimeResponse


class FactionCrimeId(BaseQuery):
    """
    A collection of paths representing `FactionCrimeId`.
    """

    crime = Path(
        "/faction/{crimeId}/crime",
        FactionCrimeResponse,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{crimeId}/crime`: Get a specific organized crime
    Requires minimal access key with faction API access permissions.

    # Parameters
    - crimeId : Crime id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="faction/{crimeId}")

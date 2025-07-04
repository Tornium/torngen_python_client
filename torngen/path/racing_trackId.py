from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.racing_track_records_response import RacingTrackRecordsResponse


class RacingTrackId(BaseQuery):
    """
    A collection of paths representing `RacingTrackId`.

    Paths
    -----
    - `/racing/{trackId}/records` : Get track records


    `/racing/{trackId}/records`
    -------------
    Get track records
    Requires public access key. <br>Returns a list of 5 best lap records for the chosen track and car class.

    # Parameters
    - trackId : Track id
    - cat : Car class
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    records = Path(
        "/racing/{trackId}/records",
        RacingTrackRecordsResponse,
        trackId=Parameter("trackId", "path", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="racing/{trackId}")

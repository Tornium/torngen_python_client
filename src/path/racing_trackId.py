from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class RacingTrackId(BaseQuery):
    """
    A collection of paths representing `RacingTrackId`.

    Paths
    -----
    /racing/{trackId}/records : Get track records
    """

    records = Path(
        "/racing/{trackId}/records",
        None,
        trackId=Parameter("trackId", "path", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

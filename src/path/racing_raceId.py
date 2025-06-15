from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class RacingRaceId(BaseQuery):
    """
    A collection of paths representing `RacingRaceId`.

    Paths
    -----
    /racing/{raceId}/race : Get specific race details
    """

    race = Path(
        "/racing/{raceId}/race",
        None,
        raceId=Parameter("raceId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

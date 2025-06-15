from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class FactionRankedWarId(BaseQuery):
    """
    A collection of paths representing `FactionRankedWarId`.

    Paths
    -----
    /faction/{rankedWarId}/rankedwarreport : Get ranked war details
    """

    rankedwarreport = Path(
        "/faction/{rankedWarId}/rankedwarreport",
        None,
        rankedWarId=Parameter("rankedWarId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

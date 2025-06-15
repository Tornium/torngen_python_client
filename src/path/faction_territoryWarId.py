from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class FactionTerritoryWarId(BaseQuery):
    """
    A collection of paths representing `FactionTerritoryWarId`.

    Paths
    -----
    /faction/{territoryWarId}/territorywarreport : Get territory war details
    """

    territorywarreport = Path(
        "/faction/{territoryWarId}/territorywarreport",
        None,
        territoryWarId=Parameter(
            "territoryWarId", "path", required=True, deprecated=False
        ),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

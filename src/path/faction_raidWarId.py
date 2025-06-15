from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class FactionRaidWarId(BaseQuery):
    """
    A collection of paths representing `FactionRaidWarId`.

    Paths
    -----
    /faction/{raidWarId}/raidreport : Get raid war details
    """

    raidreport = Path(
        "/faction/{raidWarId}/raidreport",
        None,
        raidWarId=Parameter("raidWarId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

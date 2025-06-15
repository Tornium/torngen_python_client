from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class FactionChainId(BaseQuery):
    """
    A collection of paths representing `FactionChainId`.

    Paths
    -----
    /faction/{chainId}/chainreport : Get a chain report
    """

    chainreport = Path(
        "/faction/{chainId}/chainreport",
        None,
        chainId=Parameter("chainId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

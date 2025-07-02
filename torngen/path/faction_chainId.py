from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_chain_report_response import FactionChainReportResponse


class FactionChainId(BaseQuery):
    """
    A collection of paths representing `FactionChainId`.

    Paths
    -----
    - `/faction/{chainId}/chainreport` : Get a chain report


    `/faction/{chainId}/chainreport`
    -------------
    Get a chain report
    Requires public access key. <br> Chain reports for ongoing chains are available only for your own faction.

    # Parameters
    - chainId : Chain id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    chainreport = Path(
        "/faction/{chainId}/chainreport",
        FactionChainReportResponse,
        chainId=Parameter("chainId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="faction/{chainId}")

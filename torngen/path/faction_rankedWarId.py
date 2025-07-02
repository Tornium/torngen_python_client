from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_ranked_war_report_response import \
    FactionRankedWarReportResponse


class FactionRankedWarId(BaseQuery):
    """
    A collection of paths representing `FactionRankedWarId`.

    Paths
    -----
    - `/faction/{rankedWarId}/rankedwarreport` : Get ranked war details


    `/faction/{rankedWarId}/rankedwarreport`
    -------------
    Get ranked war details
    Requires public access key. <br>

    # Parameters
    - rankedWarId : Ranked war id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    rankedwarreport = Path(
        "/faction/{rankedWarId}/rankedwarreport",
        FactionRankedWarReportResponse,
        rankedWarId=Parameter("rankedWarId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="faction/{rankedWarId}")

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_territory_war_report_response import (
    FactionTerritoryWarReportResponse,
)


class FactionTerritoryWarId(BaseQuery):
    """
    A collection of paths representing `FactionTerritoryWarId`.

    Paths
    -----
    - `/faction/{territoryWarId}/territorywarreport` : Get territory war details


    `/faction/{territoryWarId}/territorywarreport`
    -------------
    Get territory war details
    Requires public access key. <br>

    # Parameters
    - territoryWarId : Territory war id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    territorywarreport = Path(
        "/faction/{territoryWarId}/territorywarreport",
        FactionTerritoryWarReportResponse,
        territoryWarId=Parameter(
            "territoryWarId", "path", required=True, deprecated=False
        ),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="faction/{territoryWarId}")

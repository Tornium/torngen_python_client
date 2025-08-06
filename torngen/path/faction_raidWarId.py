from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_raid_war_report_response import FactionRaidWarReportResponse


class FactionRaidWarId(BaseQuery):
    """
    A collection of paths representing `FactionRaidWarId`.
    """

    raidreport = Path(
        "/faction/{raidWarId}/raidreport",
        FactionRaidWarReportResponse,
        raidWarId=Parameter("raidWarId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{raidWarId}/raidreport`: Get raid war details
    Requires public access key.

    # Parameters
    - raidWarId : Raid war id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="faction/{raidWarId}")

from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.faction_crime_response import FactionCrimeResponse
from ..schema.faction_oc_history_response import FactionOcHistoryResponse


class FactionCrimeId(BaseQuery):
    """
    A collection of paths representing `FactionCrimeId`.
    """

    crime = Path(
        "/faction/{crimeId}/crime",
        FactionCrimeResponse,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{crimeId}/crime`: Get a specific organized crime
    Requires minimal access key with faction API access permissions.

    # Parameters
    - crimeId : Crime id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    ochistory = Path(
        "/faction/{crimeId}/ochistory",
        FactionOcHistoryResponse,
        crimeId=Parameter("crimeId", "path", required=True, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{crimeId}/ochistory`: Get the history of a specific organized crime
    Requires limited access key with faction API access permissions. Only available for organized crimes of your current faction. Entries are ordered from newest to oldest, limited to the latest 500. The 'details' field depends on the 'action': * 'Joined', 'Left' & 'Kicked' return 'FactionOcHistoryRoleDetails'. * 'RoleChanged' returns 'FactionOcHistoryRoleChangeDetails'. * 'Spawned' returns 'FactionOcHistorySpawnDetails'. * 'ItemUsed' & 'ItemLost' return 'FactionOcHistoryItem'. * 'Jailed' & 'Hospitalized' return 'FactionOcHistoryPunishmentDetails'. * 'Injured' returns 'FactionOcHistoryInjuryDetails'. * 'Payout' returns 'FactionOcHistoryPayoutDetails'. * 'PayoutReceived' returns 'FactionOcHistoryPayoutReceivedDetails'. * 'Completed', 'Failed' & 'Expired' return null.

    # Parameters
    - crimeId : Crime id
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="faction/{crimeId}")

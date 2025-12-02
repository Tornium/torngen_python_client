from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.torn_item_details_response import TornItemDetailsResponse


class TornId(BaseQuery):
    """
    A collection of paths representing `TornId`.
    """

    itemdetails = Path(
        "/torn/{id}/itemdetails",
        TornItemDetailsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/torn/{id}/itemdetails`: Get information about a specific item
    Requires public key.

    # Parameters
    - id : Item uid
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="torn/{id}")

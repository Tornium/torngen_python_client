from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.torn_items_response import TornItemsResponse


class TornIds(BaseQuery):
    """
    A collection of paths representing `TornIds`.
    """

    items = Path(
        "/torn/{ids}/items",
        TornItemsResponse,
        ids=Parameter("ids", "path", required=True, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/torn/{ids}/items`: Get information about items
    Requires public key.<br>Details are always populated when available.

    # Parameters
    - ids : Item id or a list of item ids (comma separated)
    - sort : Sort rows from newest to oldest Default ordering is ascending
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="torn/{ids}")

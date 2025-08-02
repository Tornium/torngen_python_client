from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.torn_log_types_response import TornLogTypesResponse


class TornLogCategoryId(BaseQuery):
    """
    A collection of paths representing `TornLogCategoryId`.
    """

    logtypes = Path(
        "/torn/{logCategoryId}/logtypes",
        TornLogTypesResponse,
        logCategoryId=Parameter(
            "logCategoryId", "path", required=True, deprecated=False
        ),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/torn/{logCategoryId}/logtypes`: Get available log ids for a specific log category
    Requires public key.

    # Parameters
    - logCategoryId : Log category id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="torn/{logCategoryId}")

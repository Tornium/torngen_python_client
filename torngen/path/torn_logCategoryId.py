from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class TornLogCategoryId(BaseQuery):
    """
    A collection of paths representing `TornLogCategoryId`.

    Paths
    -----
    - `/torn/{logCategoryId}/logtypes` : Get available log ids for a specific log category


    `/torn/{logCategoryId}/logtypes`
    -------------
    Get available log ids for a specific log category
    Requires public key. <br>

    # Parameters
    - logCategoryId : Log category id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    logtypes = Path(
        "/torn/{logCategoryId}/logtypes",
        None,
        logCategoryId=Parameter(
            "logCategoryId", "path", required=True, deprecated=False
        ),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

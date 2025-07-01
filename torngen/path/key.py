from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Key(BaseQuery):
    """
       A collection of paths representing `Key`.

       Paths
       -----
       - `/key/info` : Get current key info
       - `/key/log` : Get current key log history


       `/key/info`
       -------------
       Get current key info
       Available for any key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/key/log`
       -------------
       Get current key log history
       Available for any key. <br>
    * This selection contains up to last 250 request logs.

       # Parameters
       - limit : N/A
       - offset : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    info = Path(
        "/key/info",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    log = Path(
        "/key/log",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

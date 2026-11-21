from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.key_info_response import KeyInfoResponse
from ..schema.key_log_response import KeyLogResponse


class Key(BaseQuery):
    """
    A collection of paths representing `Key`.
    """

    info = Path(
        "/key/info",
        KeyInfoResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/key/info`: Get current key info
    Available for any key. 'sensitive_data' is true when the key returns the same data as a Limited Access key (e.g. battle stats, revive setting, property and company finances): Limited Access, Full Access and custom keys created with 'Include sensitive data' enabled. Custom keys created before this option existed keep the permissions they had, report false and have 'legacy_permissions' set to true.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    log = Path(
        "/key/log",
        KeyLogResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/key/log`: Get current key log history
    Available for any key. * This selection contains up to last 250 request logs.

    # Parameters
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="key")

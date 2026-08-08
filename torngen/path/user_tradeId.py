from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.user_trade_response import UserTradeResponse


class UserTradeId(BaseQuery):
    """
    A collection of paths representing `UserTradeId`.
    """

    trade = Path(
        "/user/{tradeId}/trade",
        UserTradeResponse,
        tradeId=Parameter("tradeId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/user/{tradeId}/trade`: Get your detailed trade
    Requires limited access key. Only possible to get trades you participated in.

    # Parameters
    - tradeId : Trade id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="user/{tradeId}")

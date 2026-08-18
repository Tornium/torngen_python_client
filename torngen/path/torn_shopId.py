from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.torn_city_shops_response import TornCityShopsResponse


class TornShopId(BaseQuery):
    """
    A collection of paths representing `TornShopId`.
    """

    cityshops = Path(
        "/torn/{shopId}/cityshops",
        TornCityShopsResponse,
        shopId=Parameter("shopId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/torn/{shopId}/cityshops`: Get stock information for a specific shop
    Requires public access key.

    # Parameters
    - shopId : Shop id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="torn/{shopId}")

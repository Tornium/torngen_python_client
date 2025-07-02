from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.user_property_response import UserPropertyResponse


class PropertyId(BaseQuery):
    """
    A collection of paths representing `PropertyId`.

    Paths
    -----
    - `/property/{id}/property` : Get a specific property


    `/property/{id}/property`
    -------------
    Get a specific property
    Requires public access key. <br>

    # Parameters
    - id : Property id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    property = Path(
        "/property/{id}/property",
        UserPropertyResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="property/{id}")

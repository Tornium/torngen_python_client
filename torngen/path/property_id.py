from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.property_property_response import PropertyPropertyResponse


class PropertyId(BaseQuery):
    """
    A collection of paths representing `PropertyId`.
    """

    property = Path(
        "/property/{id}/property",
        PropertyPropertyResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/property/{id}/property`: Get a specific property
    Requires public access key.

    # Parameters
    - id : Property id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="property/{id}")

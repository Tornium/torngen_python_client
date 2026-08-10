from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.companies_response import CompaniesResponse


class CompanyTypeId(BaseQuery):
    """
    A collection of paths representing `CompanyTypeId`.
    """

    companies = Path(
        "/company/{typeId}/companies",
        CompaniesResponse,
        typeId=Parameter("typeId", "path", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/{typeId}/companies`: Get a list of companies for a specific company type
    Requires public access key.

    # Parameters
    - typeId : Company type id
    - limit : N/A
    - offset : N/A
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="company/{typeId}")

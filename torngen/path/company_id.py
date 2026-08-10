from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.company_employees_response_basic import CompanyEmployeesResponseBasic
from ..schema.company_profile_response import CompanyProfileResponse


class CompanyId(BaseQuery):
    """
    A collection of paths representing `CompanyId`.
    """

    profile = Path(
        "/company/{id}/profile",
        CompanyProfileResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/{id}/profile`: Get a company's profile
    Requires public access key.

    # Parameters
    - id : Company id
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    employees = Path(
        "/company/{id}/employees",
        CompanyEmployeesResponseBasic,
        id=Parameter("id", "path", required=True, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/{id}/employees`: Get a company's employees
    Requires public access key.

    # Parameters
    - id : Company id
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="company/{id}")

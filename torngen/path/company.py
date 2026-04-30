from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.company_applications_response import CompanyApplicationsResponse
from ..schema.company_employees_response import CompanyEmployeesResponse
from ..schema.company_lookup_response import CompanyLookupResponse
from ..schema.company_profile_response_mixed import CompanyProfileResponseMixed
from ..schema.company_stock_response import CompanyStockResponse
from ..schema.timestamp_response import TimestampResponse


class Company(BaseQuery):
    """
    A collection of paths representing `Company`.
    """

    lookup = Path(
        "/company/lookup",
        CompanyLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/lookup`: N/A
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    profile = Path(
        "/company/profile",
        CompanyProfileResponseMixed,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/profile`: Get my company's profile
    Requires public access key. When using Limited, Custom or Full access API keys, the response will be of type CompanyProfileExtended, otherwise it will be CompanyProfile.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    timestamp = Path(
        "/company/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/timestamp`: Get current server time
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    stock = Path(
        "/company/stock",
        CompanyStockResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/stock`: Get your company's stock
    Requires limited access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    applications = Path(
        "/company/applications",
        CompanyApplicationsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/applications`: Get your company's applications
    Requires limited access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    employees = Path(
        "/company/employees",
        CompanyEmployeesResponse,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/employees`: Get my company's employees
    Requires public access key. When using Limited, Custom or Full access API keys, the response will be of type CompanyEmployeeExtended, otherwise it will be of type CompanyEmployee.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="company")

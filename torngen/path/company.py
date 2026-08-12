from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.companies_search_response import CompaniesSearchResponse
from ..schema.company_applications_response import CompanyApplicationsResponse
from ..schema.company_employees_response import CompanyEmployeesResponse
from ..schema.company_lookup_response import CompanyLookupResponse
from ..schema.company_profile_response_mixed import CompanyProfileResponseMixed
from ..schema.company_stock_response import CompanyStockResponse
from ..schema.news_response import NewsResponse
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

    news = Path(
        "/company/news",
        NewsResponse,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/news`: Get your company's news details
    Requires minimal access key.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - cat : News category type
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
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
    Requires public access key. When using Limited, Custom or Full access API keys, the response will be: * for director: CompanyEmployeeFull * for employee: CompanyEmployeeExtended * anyone else: CompanyEmployee.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    search = Path(
        "/company/search",
        CompaniesSearchResponse,
        name=Parameter("name", "query", required=False, deprecated=False),
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/company/search`: Search companies by name or other criteria
    Requires public access key. This selection is standalone and cannot be used together with other selections.

    # Parameters
    - name : Name to search for.
    - filters : A filtering query parameter allowing a comma-separated list of filters.    *  Each filter can be one of the following:  *  Fixed options: `recruiting`, `notRecruiting`  *  Dynamic options: `fieldName`+`condition`+`number`. Each dynamic filter is made out of 3 parts separated by colon `:`:  *  * `fieldName` is one of: `id`, `type`, `daysOld`, `rating`, `dailyIncome`, `weeklyIncome`, `dailyCustomers`, `weeklyCustomers`  *  * `condition` is one of: `=`, `!=`, `&lt;`, `&lt;=`, `&gt;=`, `&gt;`, `Equal`, `NotEqual`, `Less`, `LessOrEqual`, `GreaterOrEqual`, `Greater`  *  * `number`: any integer value  *  Examples:  * `filters=recruiting`,  * `filters=weeklyIncome:&gt;=:20000,id:&lt;:1000,notRecruiting`,  * `filters=type:Equal:10,rating:=:10,dailyIncome:&lt;=:6666666`
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="company")

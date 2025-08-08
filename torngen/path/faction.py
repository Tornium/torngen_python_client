from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_applications_response import FactionApplicationsResponse
from ..schema.faction_attacks_full_response import FactionAttacksFullResponse
from ..schema.faction_attacks_response import FactionAttacksResponse
from ..schema.faction_balance_response import FactionBalanceResponse
from ..schema.faction_basic_response import FactionBasicResponse
from ..schema.faction_chain_report_response import FactionChainReportResponse
from ..schema.faction_chains_response import FactionChainsResponse
from ..schema.faction_contributors_response import FactionContributorsResponse
from ..schema.faction_crimes_response import FactionCrimesResponse
from ..schema.faction_hof_response import FactionHofResponse
from ..schema.faction_lookup_response import FactionLookupResponse
from ..schema.faction_members_response import FactionMembersResponse
from ..schema.faction_news_response import FactionNewsResponse
from ..schema.faction_ongoing_chain_response import FactionOngoingChainResponse
from ..schema.faction_positions_response import FactionPositionsResponse
from ..schema.faction_rackets_response import FactionRacketsResponse
from ..schema.faction_raids_response import FactionRaidsResponse
from ..schema.faction_ranked_war_response import FactionRankedWarResponse
from ..schema.faction_search_response import FactionSearchResponse
from ..schema.faction_stats_response import FactionStatsResponse
from ..schema.faction_territories_ownership_response import (
    FactionTerritoriesOwnershipResponse,
)
from ..schema.faction_territories_response import FactionTerritoriesResponse
from ..schema.faction_territory_wars_response import FactionTerritoryWarsResponse
from ..schema.faction_upgrades_response import FactionUpgradesResponse
from ..schema.faction_warfare_response import FactionWarfareResponse
from ..schema.faction_wars_response import FactionWarsResponse
from ..schema.reports_response import ReportsResponse
from ..schema.revives_full_response import RevivesFullResponse
from ..schema.revives_response import RevivesResponse
from ..schema.timestamp_response import TimestampResponse


class Faction(BaseQuery):
    """
    A collection of paths representing `Faction`.
    """

    revives = Path(
        "/faction/revives",
        RevivesResponse,
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/revives`: Get your faction's detailed revives
    Requires limited access key with faction API access permissions.

    # Parameters
    - filters : It&#39;s possible to use this query parameter to only get incoming or outgoing revives. If not specified, this selection will return both incoming and outgoing revives.
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    search = Path(
        "/faction/search",
        FactionSearchResponse,
        name=Parameter("name", "query", required=False, deprecated=False),
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/search`: Search factions by name or other criteria
    Requires public access key. This selection is standalone and cannot be used together with other selections.

    # Parameters
    - name : Name  to search for.
    - filters : A filtering query parameter allowing a comma-separated list of filters.    * Each filter can be one of the following:  * Fixed options: &#39;destroyed&#39;, &#39;notDestroyed&#39;, &#39;recruiting&#39;, &#39;notRecruiting&#39;  * Dynamic options: `fieldName`+`condition`+`number`, where:  * * `fieldName` is one of: `id`, `respect`, `members`  * * `condition` is one of: `Equal`, `NotEqual`, `Less`, `LessOrEqual`, `GreaterOrEqual`, `Greater`  * * `number`: any integer value  * Examples: `filters=destroyed`, `filters=notDestroyed,recruiting`, `filters=respectLessOrEqual20000,idGreater100,notRecruiting`
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    news = Path(
        "/faction/news",
        FactionNewsResponse,
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
    `/faction/news`: Get your faction's news details
    Requires minimal access key with faction API access permissions. It is possible to pass up to 10 categories at the time (comma separated). Categories 'attack', 'depositFunds' and 'giveFunds' are only available with 'Custom', 'Limited' or 'Full' access keys.

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

    rankedwars = Path(
        "/faction/rankedwars",
        FactionRankedWarResponse,
        cat=Parameter("cat", "query", required=False, deprecated=True),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/rankedwars`: Get ranked wars history for your faction
    Requires public access key.

    # Parameters
    - cat : This parameter is deprecated. The ranked wars list can now instead be fetched via &#39;faction&#39; -&gt; &#39;warfare&#39; endpoint. This functionality will be removed on 1st of September 2025. (DEPRECATED) 
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - sort : Sorted by the greatest timestamps
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    lookup = Path(
        "/faction/lookup",
        FactionLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/lookup`: N/A
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    revivesFull = Path(
        "/faction/revivesFull",
        RevivesFullResponse,
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/revivesFull`: Get your faction's simplified revives
    Requires limited access key with faction API access permissions.

    # Parameters
    - filters : It&#39;s possible to use this query parameter to only get incoming or outgoing revives. If not specified, this selection will return both incoming and outgoing revives.
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    reports = Path(
        "/faction/reports",
        ReportsResponse,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        target=Parameter("target", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/reports`: Get faction reports
    Requires limited access key. * The default limit is set to 25. However, the limit can be set to 100 for the 'stats' category.

    # Parameters
    - cat : Used to filter reports with a specific type.
    - target : Get reports for a specific player by passing their player ID.
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    hof = Path(
        "/faction/hof",
        FactionHofResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/hof`: Get your faction's hall of fame rankings.
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    wars = Path(
        "/faction/wars",
        FactionWarsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/wars`: Get your faction's wars & pacts details
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    chain = Path(
        "/faction/chain",
        FactionOngoingChainResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/chain`: Get your faction's current chain
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    territory = Path(
        "/faction/territory",
        FactionTerritoriesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/territory`: Get a list of your faction's territories
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    members = Path(
        "/faction/members",
        FactionMembersResponse,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/members`: Get a list of your faction's members
    Requires public access key. The 'revive_setting' value will be populated (not Unknown) if you have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    timestamp = Path(
        "/faction/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/timestamp`: Get current server time
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    rackets = Path(
        "/faction/rackets",
        FactionRacketsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/rackets`: Get a list of current rackets
    Requires public access key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    applications = Path(
        "/faction/applications",
        FactionApplicationsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/applications`: Get your faction's applications
    Requires minimal access key with faction API access permissions.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    basic = Path(
        "/faction/basic",
        FactionBasicResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/basic`: Get your faction's basic details
    Requires public access key. The 'is_enlisted' value will be populated if you have API faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    chainreport = Path(
        "/faction/chainreport",
        FactionChainReportResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/chainreport`: Get your faction's latest chain report
    Requires public access key. This includes currently ongoing chains.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    attacksfull = Path(
        "/faction/attacksfull",
        FactionAttacksFullResponse,
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/attacksfull`: Get your faction's simplified attacks
    Requires limited access key with faction API access permissions.

    # Parameters
    - filters : It&#39;s possible to use this query parameter to only get incoming or outgoing attacks. If not specified, this selection will return both incoming and outgoing attacks.
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    positions = Path(
        "/faction/positions",
        FactionPositionsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/positions`: Get your faction's positions details
    Requires minimal access key with faction API access permissions.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    attacks = Path(
        "/faction/attacks",
        FactionAttacksResponse,
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/attacks`: Get your faction's detailed attacks
    Requires limited access key with faction API access permissions.

    # Parameters
    - filters : It&#39;s possible to use this query parameter to only get incoming or outgoing attacks. If not specified, this selection will return both incoming and outgoing attacks.
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    warfare = Path(
        "/faction/warfare",
        FactionWarfareResponse,
        cat=Parameter("cat", "query", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/warfare`: Get faction warfare
    Requires public access key. The response depends on the selected category.

    # Parameters
    - cat : N/A
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    chains = Path(
        "/faction/chains",
        FactionChainsResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/chains`: Get a list of your faction's completed chains
    Requires public access key.

    # Parameters
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    balance = Path(
        "/faction/balance",
        FactionBalanceResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/balance`: Get your faction's & member's balance details
    Requires limited access key with faction API access permissions.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Limited). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    contributors = Path(
        "/faction/contributors",
        FactionContributorsResponse,
        stat=Parameter("stat", "query", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/contributors`: Get your faction's challenge contributors
    Requires limiteed access key with faction API access permissions.

    # Parameters
    - stat : Get contributors for this field.
    - cat : By default, this selection will return only current faction&#39;s member contributions, and the option &#39;all&#39; will return all contributors.
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    raids = Path(
        "/faction/raids",
        FactionRaidsResponse,
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/raids`: Get raids history for your faction
    Requires public access key.

    # Parameters
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - sort : Sorted by the greatest timestamps
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    territorywars = Path(
        "/faction/territorywars",
        FactionTerritoryWarsResponse,
        cat=Parameter("cat", "query", required=False, deprecated=True),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/territorywars`: Get territory wars history for your faction
    Requires public access key.

    # Parameters
    - cat : This parameter is deprecated. The territory wars list can now instead be fetched via &#39;faction&#39; -&gt; &#39;warfare&#39; endpoint. This functionality will be removed on 1st of September 2025. (DEPRECATED) 
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - sort : Sorted by the greatest timestamps
    - limit : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    stats = Path(
        "/faction/stats",
        FactionStatsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/stats`: Get your faction's challenges stats
    Requires minimal access key with faction API access permissions.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    territoryownership = Path(
        "/faction/territoryownership",
        FactionTerritoriesOwnershipResponse,
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/territoryownership`: Get a list of your faction's territories
    Requires public access key.

    # Parameters
    - offset : N/A
    - limit : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    upgrades = Path(
        "/faction/upgrades",
        FactionUpgradesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/upgrades`: Get your faction's upgrades
    Requires minimal access key with faction API access permissions.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    crimes = Path(
        "/faction/crimes",
        FactionCrimesResponse,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        filters=Parameter("filters", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/crimes`: Get your faction's organized crimes
    Requires minimal access key with faction API access permissions. It's possible to get older entries either by timestamp range (from, to) or with offset. Crimes are ordered depending on the category chosen: * For categories 'all' & 'available', the ordering field is 'created_at'. * For categories 'successful', 'failed' & 'completed', the ordering field is 'executed_at'. * For categories 'recruiting' & 'expired', the ordering field is 'expired_at'. * For category 'planning', the ordering field is 'ready_at'.

    # Parameters
    - cat : Category of organized crimes returned. Category &#39;available&#39; includes both &#39;recruiting&#39; &amp; &#39;planning&#39;, and category &#39;completed&#39; includes both &#39;successful&#39; &amp; &#39;failure&#39; Default category is &#39;all&#39;.
    - filters : It&#39;s possible to set this parameter to specify a field used for the sort, from &amp; to query parameters. If not specified, the field will default to the category sorting as described above.
    - offset : N/A
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - sort : Sorted by the greatest timestamps
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Minimal). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="faction")

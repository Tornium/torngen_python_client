from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Faction(BaseQuery):
    """
       A collection of paths representing `Faction`.

       Paths
       -----
       - `/faction/revives` : Get your faction's detailed revives
       - `/faction/search` : Search factions by name or other criteria
       - `/faction/news` : Get your faction's news details
       - `/faction/rankedwars` : Get ranked wars history for your faction
       - `/faction/lookup` : N/A
       - `/faction/revivesFull` : Get your faction's simplified revives
       - `/faction/reports` : Get faction reports
       - `/faction/hof` : Get your faction's hall of fame rankings.
       - `/faction/wars` : Get your faction's wars & pacts details
       - `/faction/chain` : Get your faction's current chain
       - `/faction/territory` : Get a list of your faction's territories
       - `/faction/members` : Get a list of your faction's members
       - `/faction/timestamp` : Get current server time
       - `/faction/rackets` : Get a list of current rackets
       - `/faction/applications` : Get your faction's applications
       - `/faction/basic` : Get your faction's basic details
       - `/faction/chainreport` : Get your faction's latest chain report
       - `/faction/attacksfull` : Get your faction's simplified attacks
       - `/faction/positions` : Get your faction's positions details
       - `/faction/attacks` : Get your faction's detailed attacks
       - `/faction/warfare` : Get faction warfare
       - `/faction/chains` : Get a list of your faction's completed chains
       - `/faction/balance` : Get your faction's & member's balance details
       - `/faction/contributors` : Get your faction's challenge contributors
       - `/faction/raids` : Get raids history for your faction
       - `/faction/territorywars` : Get territory wars history for your faction
       - `/faction/stats` : Get your faction's challenges stats
       - `/faction/territoryownership` : Get a list of your faction's territories
       - `/faction/upgrades` : Get your faction's upgrades
       - `/faction/crimes` : Get your faction's organized crimes


       `/faction/revives`
       -------------
       Get your faction's detailed revives
       Requires limited access key with faction API access permissions. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/search`
       -------------
       Search factions by name or other criteria
       Requires public access key. <br>This selection is standalone and cannot be used together with other selections.

       # Parameters
       - name : Name  to search for.
       - filters : A filtering query parameter allowing a comma-separated list of filters.    * Each filter can be one of the following:  * Fixed options: 'destroyed', 'notDestroyed', 'recruiting', 'notRecruiting'  * Dynamic options: `fieldName`+`condition`+`number`, where:  * * `fieldName` is one of: `id`, `respect`, `members`  * * `condition` is one of: `Equal`, `NotEqual`, `Less`, `LessOrEqual`, `GreaterOrEqual`, `Greater`  * * `number`: any integer value  * Examples: `filters=destroyed`, `filters=notDestroyed,recruiting`, `filters=respectLessOrEqual20000,idGreater100,notRecruiting`
       - limit : N/A
       - offset : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/news`
       -------------
       Get your faction's news details
       Requires minimal access key with faction API access permissions. <br> It is possible to pass up to 10 categories at the time (comma separated). Categories 'attack', 'depositFunds' and 'giveFunds' are only available with 'Custom', 'Limited' or 'Full' access keys.

       # Parameters
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - cat : News category type
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/rankedwars`
       -------------
       Get ranked wars history for your faction
       Requires public access key. <br>

       # Parameters
       - cat : This parameter is deprecated. The ranked wars list can now instead be fetched via 'faction' -> 'warfare' endpoint. This functionality will be removed on 1st of September 2025. (DEPRECATED)
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - sort : Sorted by the greatest timestamps
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/lookup`
       -------------

       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/revivesFull`
       -------------
       Get your faction's simplified revives
       Requires limited access key with faction API access permissions. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/reports`
       -------------
       Get faction reports
       Requires limited access key. <br>
    *  The default limit is set to 25. However, the limit can be set to 100 for the 'stats' category.

       # Parameters
       - cat : Used to filter reports with a specific type.
       - target : Get reports for a specific player by passing their player ID.
       - limit : N/A
       - offset : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/hof`
       -------------
       Get your faction's hall of fame rankings.
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/wars`
       -------------
       Get your faction's wars & pacts details
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/chain`
       -------------
       Get your faction's current chain
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/territory`
       -------------
       Get a list of your faction's territories
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/members`
       -------------
       Get a list of your faction's members
       Requires public access key. <br> The 'revive_setting' value will be populated (not Unknown) if you have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

       # Parameters
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/timestamp`
       -------------
       Get current server time
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/rackets`
       -------------
       Get a list of current rackets
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/applications`
       -------------
       Get your faction's applications
       Requires minimal access key with faction API access permissions. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/basic`
       -------------
       Get your faction's basic details
       Requires public access key. <br> The 'is_enlisted' value will be populated if you have API faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/chainreport`
       -------------
       Get your faction's latest chain report
       Requires public access key. <br> This includes currently ongoing chains.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/attacksfull`
       -------------
       Get your faction's simplified attacks
       Requires limited access key with faction API access permissions. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/positions`
       -------------
       Get your faction's positions details
       Requires minimal access key with faction API access permissions. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/attacks`
       -------------
       Get your faction's detailed attacks
       Requires limited access key with faction API access permissions. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/warfare`
       -------------
       Get faction warfare
       Requires public access key. <br>The response depends on the selected category.

       # Parameters
       - cat : N/A
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/chains`
       -------------
       Get a list of your faction's completed chains
       Requires public access key. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/balance`
       -------------
       Get your faction's & member's balance details
       Requires limited access key with faction API access permissions. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/contributors`
       -------------
       Get your faction's challenge contributors
       Requires limiteed access key with faction API access permissions. <br>

       # Parameters
       - stat : Get contributors for this field.
       - cat : By default, this selection will return only current faction's member contributions, and the option 'all' will return all contributors.
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/raids`
       -------------
       Get raids history for your faction
       Requires public access key. <br>

       # Parameters
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - sort : Sorted by the greatest timestamps
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/territorywars`
       -------------
       Get territory wars history for your faction
       Requires public access key. <br>

       # Parameters
       - cat : This parameter is deprecated. The territory wars list can now instead be fetched via 'faction' -> 'warfare' endpoint. This functionality will be removed on 1st of September 2025. (DEPRECATED)
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - sort : Sorted by the greatest timestamps
       - limit : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/stats`
       -------------
       Get your faction's challenges stats
       Requires minimal access key with faction API access permissions. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/territoryownership`
       -------------
       Get a list of your faction's territories
       Requires public access key. <br>

       # Parameters
       - offset : N/A
       - limit : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/upgrades`
       -------------
       Get your faction's upgrades
       Requires minimal access key with faction API access permissions. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/faction/crimes`
       -------------
       Get your faction's organized crimes
       Requires minimal access key with faction API access permissions. <br> It's possible to get older entries either by timestamp range (from, to) or with offset.<br> Crimes are ordered depending on the category chosen:
    * For categories 'all' & 'available', the ordering field is 'created_at'.
    * For categories 'successful', 'failed' & 'completed', the ordering field is 'executed_at'.
    * For categories 'recruiting' & 'expired', the ordering field is 'expired_at'.
    * For category 'planning', the ordering field is 'ready_at'.

       # Parameters
       - cat : Category of organized crimes returned. Category 'available' includes both 'recruiting' & 'planning', and category 'completed' includes both 'successful' & 'failure' Default category is 'all'.
       - offset : N/A
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - sort : Sorted by the greatest timestamps
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    revives = Path(
        "/faction/revives",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    search = Path(
        "/faction/search",
        None,
        name=Parameter("name", "query", required=False, deprecated=False),
        filters=Parameter("filters", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    news = Path(
        "/faction/news",
        None,
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
    rankedwars = Path(
        "/faction/rankedwars",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=True),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/faction/lookup",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    revivesFull = Path(
        "/faction/revivesFull",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    reports = Path(
        "/faction/reports",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        target=Parameter("target", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    hof = Path(
        "/faction/hof",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    wars = Path(
        "/faction/wars",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    chain = Path(
        "/faction/chain",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territory = Path(
        "/faction/territory",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    members = Path(
        "/faction/members",
        None,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/faction/timestamp",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    rackets = Path(
        "/faction/rackets",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    applications = Path(
        "/faction/applications",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    basic = Path(
        "/faction/basic",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    chainreport = Path(
        "/faction/chainreport",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacksfull = Path(
        "/faction/attacksfull",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    positions = Path(
        "/faction/positions",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacks = Path(
        "/faction/attacks",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    warfare = Path(
        "/faction/warfare",
        None,
        cat=Parameter("cat", "query", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    chains = Path(
        "/faction/chains",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    balance = Path(
        "/faction/balance",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    contributors = Path(
        "/faction/contributors",
        None,
        stat=Parameter("stat", "query", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    raids = Path(
        "/faction/raids",
        None,
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territorywars = Path(
        "/faction/territorywars",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=True),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    stats = Path(
        "/faction/stats",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territoryownership = Path(
        "/faction/territoryownership",
        None,
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    upgrades = Path(
        "/faction/upgrades",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    crimes = Path(
        "/faction/crimes",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

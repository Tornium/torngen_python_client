from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class UserId(BaseQuery):
    """
       A collection of paths representing `UserId`.

       Paths
       -----
       - `/user/{id}/personalstats` : Get a player's personal stats
       - `/user/{id}/forumposts` : Get posts for a specific player
       - `/user/{id}/bounties` : Get bounties placed on a specific user
       - `/user/{id}/properties` : Get specific user's properties
       - `/user/{id}/hof` : Get hall of fame rankings for a specific player
       - `/user/{id}/property` : Get specific user's property
       - `/user/{id}/forumthreads` : Get threads for a specific player


       `/user/{id}/personalstats`
       -------------
       Get a player's personal stats
       Requires public access key. <br>
    *  UserPersonalStatsFull is returned only when this selection is requested for the key owner with Limited, Full or Custom key.
    *  UserPersonalStatsFullPublic is returned when the requested category is 'all'.
    *  UserPersonalStatsPopular is returned when the requested category is 'popular'. Please try to use UserPersonalStatsPopular over UserPersonalStatsFullPublic wherever possible in order to reduce the server load.
    *  Otherwise, UserPersonalStatsCategory is returned for the matched category.
    *  It's possible to request specific stats via 'stat' parameter. In this case the response will vary depending on the stats requested. Private stats are still available only to the key owner (with Limited or higher key).
    *  Additionally, historical stats can also be fetched via 'stat' query parameter, but 'timestamp' parameter must be provided as well. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.

       # Parameters
       - id : User id
       - cat :
       - stat : Stat names (10 maximum). Used to fetch historical stat values
       - timestamp : Returns stats until this timestamp (converted to nearest date).
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/forumposts`
       -------------
       Get posts for a specific player
       Requires public access key. <br>Returns 20 posts per page for a specific player.

       # Parameters
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - id : User id
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/bounties`
       -------------
       Get bounties placed on a specific user
       Requires public access key. <br>

       # Parameters
       - id : User id
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/properties`
       -------------
       Get specific user's properties
       Requires public access key. <br>Extended responses are available when requesting the data with Limited or higher access keys for yourself or your spouse.

       # Parameters
       - id : User id
       - offset : N/A
       - limit : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/hof`
       -------------
       Get hall of fame rankings for a specific player
       Requires public access key. <br>The battle_stats selection will be populated only when requesting selection with Limited, Full or Custom key and for yourself.

       # Parameters
       - id : User id
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/property`
       -------------
       Get specific user's property
       Requires public access key. <br>

       # Parameters
       - id : User id
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/{id}/forumthreads`
       -------------
       Get threads for a specific player
       Requires public access key. <br>Returns 100 threads per page for a specific player. When requesting data for the key owner, a field 'new_posts' is also available, indicating the amount of unread posts. Minimum API key is required for that.

       # Parameters
       - id : User id
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    personalstats = Path(
        "/user/{id}/personalstats",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        stat=Parameter("stat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumposts = Path(
        "/user/{id}/forumposts",
        None,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        id=Parameter("id", "path", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    bounties = Path(
        "/user/{id}/bounties",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    properties = Path(
        "/user/{id}/properties",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    hof = Path(
        "/user/{id}/hof",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    property = Path(
        "/user/{id}/property",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumthreads = Path(
        "/user/{id}/forumthreads",
        None,
        id=Parameter("id", "path", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class User(BaseQuery):
    """
       A collection of paths representing `User`.

       Paths
       -----
       - `/user/education` : Get your education information
       - `/user/forumfriends` : Get updates on your friends' activity
       - `/user/attacks` : Get your detailed attacks
       - `/user/bounties` : Get bounties placed on you
       - `/user/lookup` : Get all available user selections
       - `/user/forumposts` : Get your posts
       - `/user/list` : Get your friends, enemies or targets list
       - `/user/factionbalance` : Get your current faction balance
       - `/user/personalstats` : Get your personal stats
       - `/user/properties` : Get your own properties
       - `/user/property` : Get your current property
       - `/user/forumsubscribedthreads` : Get updates on threads you subscribed to
       - `/user/reports` : Get your reports
       - `/user/races` : Get user races
       - `/user/calendar` : Get your competition's event start time
       - `/user/forumfeed` : Get updates on your threads and posts
       - `/user/hof` : Get your hall of fame rankings
       - `/user/jobranks` : Get your starter job positions
       - `/user/forumthreads` : Get your threads
       - `/user/enlistedcars` : Get user enlisted cars
       - `/user/attacksfull` : Get your simplified attacks
       - `/user/timestamp` : Get current server time
       - `/user/itemmarket` : Get your item market listings for a specific item
       - `/user/organizedcrime` : Get your current ongoing organized crime
       - `/user/revives` : Get your detailed revives
       - `/user/revivesFull` : Get your simplified revives


       `/user/education`
       -------------
       Get your education information
       The response contains a list of complete eduactions and of a current education (if any).

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/forumfriends`
       -------------
       Get updates on your friends' activity
       Requires minimal access key. <br>This selection returns data visible in 'Friends' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/attacks`
       -------------
       Get your detailed attacks
       Requires limited access key. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/bounties`
       -------------
       Get bounties placed on you
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/lookup`
       -------------
       Get all available user selections
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/forumposts`
       -------------
       Get your posts
       Requires public access key. <br>Returns 20 posts per page.

       # Parameters
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/list`
       -------------
       Get your friends, enemies or targets list
       Requires limited access key. <br>

       # Parameters
       - cat : Select list type
       - limit : N/A
       - offset : N/A
       - sort : Sort rows from newest to oldest Default ordering is ascending
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/factionbalance`
       -------------
       Get your current faction balance
       Requires limited access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/personalstats`
       -------------
       Get your personal stats
       Requires public access key. <br>
    * UserPersonalStatsFull is returned only when this selection is requested with Limited, Full or Custom key access key.
    * UserPersonalStatsFullPublic is returned when the requested category is 'all'.
    * UserPersonalStatsPopular is returned when the requested category is 'popular'. Please try to use UserPersonalStatsPopular over UserPersonalStatsFullPublic wherever possible in order to reduce the server load.
    * Otherwise, UserPersonalStatsCategory is returned for the matched category.
    * It's possible to request specific stats via 'stat' parameter. In this case the response will vary depending on the stats requested. Private stats are still available only to the key owner (with Limited or higher key).
    * Additionally, historical stats can also be fetched via 'stat' query parameter, but 'timestamp' parameter must be provided as well. It's only possible to pass up to 10 historical stats at once (the rest is trimmed). When requesting historical stats the response will be of type UserPersonalStatsHistoric.

       # Parameters
       - cat : Stats category. Required unless requesting specific stats via 'stat' query parameter
       - stat : Stat names (10 maximum). Used to fetch historical stat values
       - timestamp : Returns stats until this timestamp (converted to nearest date).
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/properties`
       -------------
       Get your own properties
       Requires public access key. <br>Extended responses are available when requesting the data with Limited or higher access keys.

       # Parameters
       - offset : N/A
       - limit : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/property`
       -------------
       Get your current property
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/forumsubscribedthreads`
       -------------
       Get updates on threads you subscribed to
       Requires minimal access key. <br>This selection returns data visible in 'Subscribed Threads' section on forum page. Threads are sorted in the same way as on site.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/reports`
       -------------
       Get your reports
       Requires limited access key. <br>
    * The default limit is set to 25. However, the limit can be set to 100 for the 'stats' category.

       # Parameters
       - cat : Used to filter reports with a specific type.
       - target : Get reports for a specific player by passing their player ID.
       - limit : N/A
       - offset : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/races`
       -------------
       Get user races
       Requires minimal access key. <br>Returns a list of user races, ordered by race start timestamp.

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - cat : Category of races returned
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/calendar`
       -------------
       Get your competition's event start time
       Requires minimal access key. <br>Only available to yourself.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/forumfeed`
       -------------
       Get updates on your threads and posts
       Requires minimal access key. <br>This selection returns data visible in 'Feed' section on forum page. Feed is sorted by timestamp descending. Only a maximum of 100 rows are returned.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/hof`
       -------------
       Get your hall of fame rankings
       Requires public access key. <br>When requesting selection with Limited, Full or Custom key, battle_stats selection will be populated.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/jobranks`
       -------------
       Get your starter job positions
       Requires minimal access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/forumthreads`
       -------------
       Get your threads
       Requires public access key. <br>Returns 100 threads per page. The field 'new_posts' is also available, indicating the amount of unread posts with a Minimum API key (or higher).

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/enlistedcars`
       -------------
       Get user enlisted cars
       Requires minimal access key. <br>Returns a list of all user enlisted cars.

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/attacksfull`
       -------------
       Get your simplified attacks
       Requires limited access key. <br>Returns up to 1,000 rows. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/timestamp`
       -------------
       Get current server time
       Requires public access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/itemmarket`
       -------------
       Get your item market listings for a specific item
       Requires limited access key. <br>

       # Parameters
       - offset : N/A
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/organizedcrime`
       -------------
       Get your current ongoing organized crime
       Requires minimal access key. <br>

       # Parameters
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Minimal). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/revives`
       -------------
       Get your detailed revives
       Requires limited access key. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

       `/user/revivesFull`
       -------------
       Get your simplified revives
       Requires limited access key. <br>

       # Parameters
       - limit : N/A
       - sort : Sorted by the greatest timestamps
       - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
       - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
       - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
       - timestamp : Timestamp to bypass cache
       - comment : Comment for your tool/service/bot/website to be visible in the logs.
       - key : API key (Limited). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    education = Path(
        "/user/education",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumfriends = Path(
        "/user/forumfriends",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacks = Path(
        "/user/attacks",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    bounties = Path(
        "/user/bounties",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/user/lookup",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumposts = Path(
        "/user/forumposts",
        None,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    list = Path(
        "/user/list",
        None,
        cat=Parameter("cat", "query", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    factionbalance = Path(
        "/user/factionbalance",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    personalstats = Path(
        "/user/personalstats",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        stat=Parameter("stat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    properties = Path(
        "/user/properties",
        None,
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    property = Path(
        "/user/property",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumsubscribedthreads = Path(
        "/user/forumsubscribedthreads",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    reports = Path(
        "/user/reports",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        target=Parameter("target", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    races = Path(
        "/user/races",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    calendar = Path(
        "/user/calendar",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumfeed = Path(
        "/user/forumfeed",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    hof = Path(
        "/user/hof",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    jobranks = Path(
        "/user/jobranks",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    forumthreads = Path(
        "/user/forumthreads",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    enlistedcars = Path(
        "/user/enlistedcars",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacksfull = Path(
        "/user/attacksfull",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/user/timestamp",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    itemmarket = Path(
        "/user/itemmarket",
        None,
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    organizedcrime = Path(
        "/user/organizedcrime",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    revives = Path(
        "/user/revives",
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
    revivesFull = Path(
        "/user/revivesFull",
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

    def __init__(self):
        super().__init__()

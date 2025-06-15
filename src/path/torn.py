from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Torn(BaseQuery):
    """
    A collection of paths representing `Torn`.

    Paths
    -----
    /torn/logtypes : Get all available log ids
    /torn/attacklog : Get attack log details
    /torn/bounties : Get bounties
    /torn/education : Get education information
    /torn/itemmods : Get information about weapon upgrades
    /torn/timestamp : Get current server time
    /torn/territory : Get territory details
    /torn/factiontree : Get full faction tree
    /torn/lookup : Get all available torn selections
    /torn/itemammo : Get information about ammo
    /torn/factionhof : Get faction hall of fame positions for a specific category
    /torn/items : Get information about items
    /torn/crimes : Get crimes information
    /torn/calendar : Get calendar information
    /torn/hof : Get player hall of fame positions for a specific category
    /torn/logcategories : Get available log categories
    """

    logtypes = Path(
        "/torn/logtypes",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacklog = Path(
        "/torn/attacklog",
        None,
        log=Parameter("log", "query", required=True, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    bounties = Path(
        "/torn/bounties",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    education = Path(
        "/torn/education",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    itemmods = Path(
        "/torn/itemmods",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/torn/timestamp",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territory = Path(
        "/torn/territory",
        None,
        ids=Parameter("ids", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    factiontree = Path(
        "/torn/factiontree",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/torn/lookup",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    itemammo = Path(
        "/torn/itemammo",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    factionhof = Path(
        "/torn/factionhof",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    items = Path(
        "/torn/items",
        None,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    crimes = Path(
        "/torn/crimes",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    calendar = Path(
        "/torn/calendar",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    hof = Path(
        "/torn/hof",
        None,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    logcategories = Path(
        "/torn/logcategories",
        None,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__()

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class Faction(BaseQuery):
    """
    A collection of paths representing `Faction`.

    Paths
    -----
    /faction/revives : Get your faction's detailed revives
    /faction/search : Search factions by name or other criteria
    /faction/news : Get your faction's news details
    /faction/rankedwars : Get ranked wars history for your faction
    /faction/lookup : N/A
    /faction/revivesFull : Get your faction's simplified revives
    /faction/reports : Get faction reports
    /faction/hof : Get your faction's hall of fame rankings.
    /faction/wars : Get your faction's wars & pacts details
    /faction/chain : Get your faction's current chain
    /faction/territory : Get a list of your faction's territories
    /faction/members : Get a list of your faction's members
    /faction/timestamp : Get current server time
    /faction/rackets : Get a list of current rackets
    /faction/applications : Get your faction's applications
    /faction/basic : Get your faction's basic details
    /faction/chainreport : Get your faction's latest chain report
    /faction/attacksfull : Get your faction's simplified attacks
    /faction/positions : Get your faction's positions details
    /faction/attacks : Get your faction's detailed attacks
    /faction/warfare : Get faction warfare
    /faction/chains : Get a list of your faction's completed chains
    /faction/balance : Get your faction's & member's balance details
    /faction/contributors : Get your faction's challenge contributors
    /faction/raids : Get raids history for your faction
    /faction/territorywars : Get territory wars history for your faction
    /faction/stats : Get your faction's challenges stats
    /faction/territoryownership : Get a list of your faction's territories
    /faction/upgrades : Get your faction's upgrades
    /faction/crimes : Get your faction's organized crimes
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

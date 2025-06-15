from base_path import Path
from base_query import BaseQuery
from parameter import Parameter


class UserId(BaseQuery):
    """
    A collection of paths representing `UserId`.

    Paths
    -----
    /user/{id}/personalstats : Get a player's personal stats
    /user/{id}/forumposts : Get posts for a specific player
    /user/{id}/bounties : Get bounties placed on a specific user
    /user/{id}/hof : Get hall of fame rankings for a specific player
    /user/{id}/forumthreads : Get threads for a specific player
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
    hof = Path(
        "/user/{id}/hof",
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

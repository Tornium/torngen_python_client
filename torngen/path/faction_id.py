from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.faction_basic_response import FactionBasicResponse
from ..schema.faction_chains_response import FactionChainsResponse
from ..schema.faction_hof_response import FactionHofResponse
from ..schema.faction_members_response import FactionMembersResponse
from ..schema.faction_ongoing_chain_response import FactionOngoingChainResponse
from ..schema.faction_raids_response import FactionRaidsResponse
from ..schema.faction_ranked_war_response import FactionRankedWarResponse
from ..schema.faction_territories_response import FactionTerritoriesResponse
from ..schema.faction_territory_wars_history_response import (
    FactionTerritoryWarsHistoryResponse,
)
from ..schema.faction_wars_response import FactionWarsResponse


class FactionId(BaseQuery):
    """
    A collection of paths representing `FactionId`.

    Paths
    -----
    - `/faction/{id}/hof` : Get a faction's hall of fame rankings.
    - `/faction/{id}/wars` : Get a faction's wars & pacts details
    - `/faction/{id}/rankedwars` : Get a faction's ranked wars history
    - `/faction/{id}/chains` : Get a list of a faction's completed chains
    - `/faction/{id}/raids` : Get a faction's raids history
    - `/faction/{id}/chain` : Get a faction's current chain
    - `/faction/{id}/members` : Get a list of a faction's members
    - `/faction/{id}/territory` : Get a list of a faction's territories
    - `/faction/{id}/basic` : Get a faction's basic details
    - `/faction/{id}/territorywars` : Get a faction's territory wars history


    `/faction/{id}/hof`
    -------------
    Get a faction's hall of fame rankings.
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/wars`
    -------------
    Get a faction's wars & pacts details
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/rankedwars`
    -------------
    Get a faction's ranked wars history
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/chains`
    -------------
    Get a list of a faction's completed chains
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/raids`
    -------------
    Get a faction's raids history
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/chain`
    -------------
    Get a faction's current chain
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/members`
    -------------
    Get a list of a faction's members
    Requires public access key. <br> The 'revive_setting' value will be populated (not Unknown) if you're requesting data for your own faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

    # Parameters
    - id : Faction id
    - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/territory`
    -------------
    Get a list of a faction's territories
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/basic`
    -------------
    Get a faction's basic details
    Requires public access key. <br> The 'is_enlisted' value will be populated if you're requesting data for your faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/faction/{id}/territorywars`
    -------------
    Get a faction's territory wars history
    Requires public access key. <br>

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    hof = Path(
        "/faction/{id}/hof",
        FactionHofResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    wars = Path(
        "/faction/{id}/wars",
        FactionWarsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    rankedwars = Path(
        "/faction/{id}/rankedwars",
        FactionRankedWarResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    chains = Path(
        "/faction/{id}/chains",
        FactionChainsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    raids = Path(
        "/faction/{id}/raids",
        FactionRaidsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    chain = Path(
        "/faction/{id}/chain",
        FactionOngoingChainResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    members = Path(
        "/faction/{id}/members",
        FactionMembersResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territory = Path(
        "/faction/{id}/territory",
        FactionTerritoriesResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    basic = Path(
        "/faction/{id}/basic",
        FactionBasicResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territorywars = Path(
        "/faction/{id}/territorywars",
        FactionTerritoryWarsHistoryResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="faction/{id}")

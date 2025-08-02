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
    """

    hof = Path(
        "/faction/{id}/hof",
        FactionHofResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/hof`: Get a faction's hall of fame rankings.
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    wars = Path(
        "/faction/{id}/wars",
        FactionWarsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/wars`: Get a faction's wars & pacts details
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    rankedwars = Path(
        "/faction/{id}/rankedwars",
        FactionRankedWarResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/rankedwars`: Get a faction's ranked wars history
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

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
    """
    `/faction/{id}/chains`: Get a list of a faction's completed chains
    Requires public access key.

    # Parameters
    - id : Faction id
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    raids = Path(
        "/faction/{id}/raids",
        FactionRaidsResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/raids`: Get a faction's raids history
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    chain = Path(
        "/faction/{id}/chain",
        FactionOngoingChainResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/chain`: Get a faction's current chain
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    members = Path(
        "/faction/{id}/members",
        FactionMembersResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/members`: Get a list of a faction's members
    Requires public access key. The 'revive_setting' value will be populated (not Unknown) if you're requesting data for your own faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as 'Unknown'.

    # Parameters
    - id : Faction id
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    territory = Path(
        "/faction/{id}/territory",
        FactionTerritoriesResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/territory`: Get a list of a faction's territories
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    basic = Path(
        "/faction/{id}/basic",
        FactionBasicResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/basic`: Get a faction's basic details
    Requires public access key. The 'is_enlisted' value will be populated if you're requesting data for your faction and have faction permissions (with custom, limited or full access keys), otherwise it will be set as null.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    territorywars = Path(
        "/faction/{id}/territorywars",
        FactionTerritoryWarsHistoryResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/faction/{id}/territorywars`: Get a faction's territory wars history
    Requires public access key.

    # Parameters
    - id : Faction id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="faction/{id}")

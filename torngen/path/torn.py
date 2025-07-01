from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.attack_log_response import AttackLogResponse
from ..schema.timestamp_response import TimestampResponse
from ..schema.torn_bounties_response import TornBountiesResponse
from ..schema.torn_calendar_response import TornCalendarResponse
from ..schema.torn_crimes_response import TornCrimesResponse
from ..schema.torn_education_response import TornEducationResponse
from ..schema.torn_faction_hof_response import TornFactionHofResponse
from ..schema.torn_faction_tree_response import TornFactionTreeResponse
from ..schema.torn_hof_response import TornHofResponse
from ..schema.torn_item_ammo_response import TornItemAmmoResponse
from ..schema.torn_item_mods_response import TornItemModsResponse
from ..schema.torn_items_response import TornItemsResponse
from ..schema.torn_log_categories_response import TornLogCategoriesResponse
from ..schema.torn_log_types_response import TornLogTypesResponse
from ..schema.torn_lookup_response import TornLookupResponse
from ..schema.torn_properties import TornProperties
from ..schema.torn_territories_response import TornTerritoriesResponse


class Torn(BaseQuery):
    """
    A collection of paths representing `Torn`.

    Paths
    -----
    - `/torn/logtypes` : Get all available log ids
    - `/torn/attacklog` : Get attack log details
    - `/torn/bounties` : Get bounties
    - `/torn/properties` : Get properties details
    - `/torn/education` : Get education information
    - `/torn/itemmods` : Get information about weapon upgrades
    - `/torn/timestamp` : Get current server time
    - `/torn/territory` : Get territory details
    - `/torn/factiontree` : Get full faction tree
    - `/torn/lookup` : Get all available torn selections
    - `/torn/itemammo` : Get information about ammo
    - `/torn/factionhof` : Get faction hall of fame positions for a specific category
    - `/torn/items` : Get information about items
    - `/torn/crimes` : Get crimes information
    - `/torn/calendar` : Get calendar information
    - `/torn/hof` : Get player hall of fame positions for a specific category
    - `/torn/logcategories` : Get available log categories


    `/torn/logtypes`
    -------------
    Get all available log ids
    Requires public key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/attacklog`
    -------------
    Get attack log details
    Requires public key. <br>

    # Parameters
    - log : Code of the attack log. E.g. d51ad4fe6be884b309b142e2d1d4f807
    - offset : N/A
    - sort : Sorted by the greatest timestamps
    - striptags : Determines if fields include HTML or not ('Hospitalized by <a href=...>user</a>' vs 'Hospitalized by user').
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/bounties`
    -------------
    Get bounties
    Requires public key. <br>

    # Parameters
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/properties`
    -------------
    Get properties details
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/education`
    -------------
    Get education information
    Requires public access key.<br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/itemmods`
    -------------
    Get information about weapon upgrades
    Requires public key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/timestamp`
    -------------
    Get current server time
    Requires public key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/territory`
    -------------
    Get territory details
    Requires public access key. <br>

    # Parameters
    - ids : Specific territory id or a list of territory ids (comma separated)
    - offset : N/A
    - limit : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/factiontree`
    -------------
    Get full faction tree
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/lookup`
    -------------
    Get all available torn selections
    Requires public key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/itemammo`
    -------------
    Get information about ammo
    Requires public key.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/factionhof`
    -------------
    Get faction hall of fame positions for a specific category
    Requires public access key. <br>

    # Parameters
    - limit : N/A
    - offset : N/A
    - cat : Leaderboards category
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/items`
    -------------
    Get information about items
    Requires public key.<br>Default category is 'All'.<br>Details are not populated when requesting the category 'All'.

    # Parameters
    - cat : Item category type
    - sort : Sort rows from newest to oldest Default ordering is ascending
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/crimes`
    -------------
    Get crimes information
    Requires public access key. <br> Return the details about released crimes.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/calendar`
    -------------
    Get calendar information
    Requires public access key. <br> Get the details about competitions & events in the running year.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/hof`
    -------------
    Get player hall of fame positions for a specific category
    Requires public key.

    # Parameters
    - limit : N/A
    - offset : N/A
    - cat : Leaderboards category
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/torn/logcategories`
    -------------
    Get available log categories
    Requires public key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    logtypes = Path(
        "/torn/logtypes",
        TornLogTypesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    attacklog = Path(
        "/torn/attacklog",
        AttackLogResponse,
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
        TornBountiesResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    properties = Path(
        "/torn/properties",
        TornProperties,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    education = Path(
        "/torn/education",
        TornEducationResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    itemmods = Path(
        "/torn/itemmods",
        TornItemModsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/torn/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    territory = Path(
        "/torn/territory",
        TornTerritoriesResponse,
        ids=Parameter("ids", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    factiontree = Path(
        "/torn/factiontree",
        TornFactionTreeResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/torn/lookup",
        TornLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    itemammo = Path(
        "/torn/itemammo",
        TornItemAmmoResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    factionhof = Path(
        "/torn/factionhof",
        TornFactionHofResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    items = Path(
        "/torn/items",
        TornItemsResponse,
        cat=Parameter("cat", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    crimes = Path(
        "/torn/crimes",
        TornCrimesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    calendar = Path(
        "/torn/calendar",
        TornCalendarResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    hof = Path(
        "/torn/hof",
        TornHofResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    logcategories = Path(
        "/torn/logcategories",
        TornLogCategoriesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="torn")

from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.racing_car_upgrades_response import RacingCarUpgradesResponse
from ..schema.racing_cars_response import RacingCarsResponse
from ..schema.racing_lookup_response import RacingLookupResponse
from ..schema.racing_races_response import RacingRacesResponse
from ..schema.racing_tracks_response import RacingTracksResponse
from ..schema.timestamp_response import TimestampResponse


class Racing(BaseQuery):
    """
    A collection of paths representing `Racing`.

    Paths
    -----
    - `/racing/tracks` : Get race tracks and descriptions
    - `/racing/timestamp` : Get current server time
    - `/racing/carupgrades` : Get all possible car upgrades
    - `/racing/lookup` : Get all available racing selections
    - `/racing/cars` : Get cars and their racing stats
    - `/racing/races` : Get races


    `/racing/tracks`
    -------------
    Get race tracks and descriptions
    Requires public access key. <br>Returns the details about racing tracks.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/racing/timestamp`
    -------------
    Get current server time
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/racing/carupgrades`
    -------------
    Get all possible car upgrades
    Requires public access key. <br>Returns the details about all possible car upgrades.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/racing/lookup`
    -------------
    Get all available racing selections
    Requires public access key. <br>

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/racing/cars`
    -------------
    Get cars and their racing stats
    Requires public access key. <br>Returns the stat details about racing cars.

    # Parameters
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    `/racing/races`
    -------------
    Get races
    Requires public access key. <br>Returns a list of races, ordered by race start timestamp.

    # Parameters
    - limit : N/A
    - sort : Sorted by the greatest timestamps
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - cat : Category of races returned
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It's not required to use this parameter when passing the API key via the Authorization header.

    """

    tracks = Path(
        "/racing/tracks",
        RacingTracksResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    timestamp = Path(
        "/racing/timestamp",
        TimestampResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    carupgrades = Path(
        "/racing/carupgrades",
        RacingCarUpgradesResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    lookup = Path(
        "/racing/lookup",
        RacingLookupResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    cars = Path(
        "/racing/cars",
        RacingCarsResponse,
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    races = Path(
        "/racing/races",
        RacingRacesResponse,
        limit=Parameter("limit", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        cat=Parameter("cat", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )

    def __init__(self):
        super().__init__(base_path="racing")

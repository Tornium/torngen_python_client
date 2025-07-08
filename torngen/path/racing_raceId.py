from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.racing_race_details_response import RacingRaceDetailsResponse


class RacingRaceId(BaseQuery):
    """
    A collection of paths representing `RacingRaceId`.
    """

    race = Path(
        "/racing/{raceId}/race",
        RacingRaceDetailsResponse,
        raceId=Parameter("raceId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/racing/{raceId}/race`: Get specific race details
    Requires public access key. <br>Returns the details of a race.

    # Parameters
    - raceId : Race id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="racing/{raceId}")

from ..base_path import Path
from ..base_query import BaseQuery
from ..parameter import Parameter
from ..schema.torn_elimination_team_players_response import (
    TornEliminationTeamPlayersResponse,
)


class TornId(BaseQuery):
    """
    A collection of paths representing `TornId`.
    """

    eliminationteam = Path(
        "/torn/{id}/eliminationteam",
        TornEliminationTeamPlayersResponse,
        id=Parameter("id", "path", required=True, deprecated=False),
        limit=Parameter("limit", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/torn/{id}/eliminationteam`: Get players in a specific elimination team
    Requires public key.

    # Parameters
    - id : Elimination team id
    - limit : N/A
    - offset : N/A
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="torn/{id}")

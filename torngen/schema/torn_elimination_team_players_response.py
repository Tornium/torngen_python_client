import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .torn_elimination_team_player import TornEliminationTeamPlayer


@dataclass
class TornEliminationTeamPlayersResponse(BaseSchema):
    """
    JSON object of `TornEliminationTeamPlayersResponse`.
    """

    eliminationteam: typing.List[TornEliminationTeamPlayer]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornEliminationTeamPlayersResponse(
            eliminationteam=BaseSchema.parse(
                data.get("eliminationteam"), typing.List[TornEliminationTeamPlayer]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

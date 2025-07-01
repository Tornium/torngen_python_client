import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_chain_warfare import FactionChainWarfare
from .faction_raid_warfare import FactionRaidWarfare
from .faction_ranked_war_details import FactionRankedWarDetails
from .faction_territory_warfare import FactionTerritoryWarfare
from .faction_warfare_dirty_bomb import FactionWarfareDirtyBomb
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionWarfareResponse(BaseSchema):
    """
    JSON object of `FactionWarfareResponse`.
    """

    warfare: (
        typing.List[FactionWarfareDirtyBomb]
        | typing.List[FactionRaidWarfare]
        | typing.List[FactionChainWarfare]
        | typing.List[FactionTerritoryWarfare]
        | typing.List[FactionRankedWarDetails]
    )
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionWarfareResponse(
            warfare=BaseSchema.parse(
                data.get("warfare"),
                typing.List[FactionWarfareDirtyBomb]
                | typing.List[FactionRaidWarfare]
                | typing.List[FactionChainWarfare]
                | typing.List[FactionTerritoryWarfare]
                | typing.List[FactionRankedWarDetails],
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

import typing

from FactionChainWarfare import FactionChainWarfare
from FactionRaidWarfare import FactionRaidWarfare
from FactionRankedWarDetails import FactionRankedWarDetails
from FactionTerritoryWarfare import FactionTerritoryWarfare
from FactionWarfareDirtyBomb import FactionWarfareDirtyBomb
from RequestMetadataWithLinks import RequestMetadataWithLinks

from ..base_schema import BaseSchema


class FactionWarfareResponse(BaseSchema):

    warfare: (
        typing.List[FactionWarfareDirtyBomb]
        | typing.List[FactionRaidWarfare]
        | typing.List[FactionChainWarfare]
        | typing.List[FactionTerritoryWarfare]
        | typing.List[FactionRankedWarDetails]
    )
    _metadata: RequestMetadataWithLinks

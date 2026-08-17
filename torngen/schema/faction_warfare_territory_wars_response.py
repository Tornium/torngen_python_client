import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_territory_warfare import FactionTerritoryWarfare
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionWarfareTerritoryWarsResponse(BaseSchema):
    """
    JSON object of `FactionWarfareTerritoryWarsResponse`.
    """

    warfareterritory: typing.List[FactionTerritoryWarfare]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionWarfareTerritoryWarsResponse(
            warfareterritory=BaseSchema.parse(
                data.get("warfareterritory"), typing.List[FactionTerritoryWarfare]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

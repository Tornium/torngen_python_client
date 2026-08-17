import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_warfare import FactionRaidWarfare
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionWarfareRaidsResponse(BaseSchema):
    """
    JSON object of `FactionWarfareRaidsResponse`.
    """

    warfareraids: typing.List[FactionRaidWarfare]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionWarfareRaidsResponse(
            warfareraids=BaseSchema.parse(
                data.get("warfareraids"), typing.List[FactionRaidWarfare]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

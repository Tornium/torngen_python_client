import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_warfare import FactionRaidWarfare
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionRaidsResponse(BaseSchema):
    """
    JSON object of `FactionRaidsResponse`.
    """

    raids: typing.List[FactionRaidWarfare]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionRaidsResponse(
            raids=BaseSchema.parse(data.get("raids"), typing.List[FactionRaidWarfare]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

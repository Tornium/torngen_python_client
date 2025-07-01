import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .torn_faction_hof import TornFactionHof


@dataclass
class TornFactionHofResponse(BaseSchema):
    """
    JSON object of `TornFactionHofResponse`.
    """

    factionhof: typing.List[TornFactionHof]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornFactionHofResponse(
            factionhof=BaseSchema.parse(
                data.get("factionhof"), typing.List[TornFactionHof]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

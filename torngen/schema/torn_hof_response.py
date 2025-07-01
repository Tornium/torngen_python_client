import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .torn_hof import TornHof


@dataclass
class TornHofResponse(BaseSchema):
    """
    JSON object of `TornHofResponse`.
    """

    hof: typing.List[TornHof]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return TornHofResponse(
            hof=BaseSchema.parse(data.get("hof"), typing.List[TornHof]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .revive import Revive


@dataclass
class RevivesResponse(BaseSchema):
    """
    JSON object of `RevivesResponse`.
    """

    revives: typing.List[Revive]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return RevivesResponse(
            revives=BaseSchema.parse(data.get("revives"), typing.List[Revive]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

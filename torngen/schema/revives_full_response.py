import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .revive_simplified import ReviveSimplified


@dataclass
class RevivesFullResponse(BaseSchema):
    """
    JSON object of `RevivesFullResponse`.
    """

    revives: typing.List[ReviveSimplified]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return RevivesFullResponse(
            revives=BaseSchema.parse(
                data.get("revives"), typing.List[ReviveSimplified]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

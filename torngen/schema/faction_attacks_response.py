import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack import Attack
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionAttacksResponse(BaseSchema):
    """
    JSON object of `FactionAttacksResponse`.
    """

    attacks: typing.List[Attack]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionAttacksResponse(
            attacks=BaseSchema.parse(data.get("attacks"), typing.List[Attack]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

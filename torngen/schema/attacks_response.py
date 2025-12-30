import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack import Attack
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class AttacksResponse(BaseSchema):
    """
    JSON object of `AttacksResponse`.
    """

    attacks: typing.List[Attack]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return AttacksResponse(
            attacks=BaseSchema.parse(data.get("attacks"), typing.List[Attack]),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

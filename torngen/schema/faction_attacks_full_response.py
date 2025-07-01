import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_simplified import AttackSimplified
from .request_metadata_with_links import RequestMetadataWithLinks


@dataclass
class FactionAttacksFullResponse(BaseSchema):
    """
    JSON object of `FactionAttacksFullResponse`.
    """

    attacks: typing.List[AttackSimplified]
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return FactionAttacksFullResponse(
            attacks=BaseSchema.parse(
                data.get("attacks"), typing.List[AttackSimplified]
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

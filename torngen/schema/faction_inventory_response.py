import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_inventory_item import FactionInventoryItem
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal


@dataclass
class FactionInventoryResponse(BaseSchema):
    """
    JSON object of `FactionInventoryResponse`.
    """

    inventory_timestamp: int
    inventory: typing.List[FactionInventoryItem]
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return FactionInventoryResponse(
            inventory_timestamp=BaseSchema.parse(data.get("inventory_timestamp"), int),
            inventory=BaseSchema.parse(
                data.get("inventory"), typing.List[FactionInventoryItem]
            ),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

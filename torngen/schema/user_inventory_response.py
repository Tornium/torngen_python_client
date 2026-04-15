import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links_and_total import RequestMetadataWithLinksAndTotal
from .user_inventory import UserInventory


@dataclass
class UserInventoryResponse(BaseSchema):
    """
    JSON object of `UserInventoryResponse`.
    """

    inventory: UserInventory
    _metadata: RequestMetadataWithLinksAndTotal

    @staticmethod
    def parse(data):
        return UserInventoryResponse(
            inventory=BaseSchema.parse(data.get("inventory"), UserInventory),
            _metadata=BaseSchema.parse(
                data.get("_metadata"), RequestMetadataWithLinksAndTotal
            ),
        )

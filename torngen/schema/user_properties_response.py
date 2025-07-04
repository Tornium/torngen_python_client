import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .request_metadata_with_links import RequestMetadataWithLinks
from .user_property_basic_details import UserPropertyBasicDetails
from .user_property_details_extended import UserPropertyDetailsExtended
from .user_property_details_extended_for_rent import UserPropertyDetailsExtendedForRent
from .user_property_details_extended_for_sale import UserPropertyDetailsExtendedForSale
from .user_property_details_extended_rented import UserPropertyDetailsExtendedRented


@dataclass
class UserPropertiesResponse(BaseSchema):
    """
    JSON object of `UserPropertiesResponse`.
    """

    properties: (
        UserPropertyDetailsExtendedForSale
        | UserPropertyDetailsExtendedForRent
        | UserPropertyDetailsExtendedRented
        | UserPropertyDetailsExtended
        | UserPropertyBasicDetails
    )
    _metadata: RequestMetadataWithLinks

    @staticmethod
    def parse(data):
        return UserPropertiesResponse(
            properties=BaseSchema.parse(
                data.get("properties"),
                UserPropertyDetailsExtendedForSale
                | UserPropertyDetailsExtendedForRent
                | UserPropertyDetailsExtendedRented
                | UserPropertyDetailsExtended
                | UserPropertyBasicDetails,
            ),
            _metadata=BaseSchema.parse(data.get("_metadata"), RequestMetadataWithLinks),
        )

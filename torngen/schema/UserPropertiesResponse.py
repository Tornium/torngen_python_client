import typing

from RequestMetadataWithLinks import RequestMetadataWithLinks
from UserPropertyBasicDetails import UserPropertyBasicDetails
from UserPropertyDetailsExtended import UserPropertyDetailsExtended
from UserPropertyDetailsExtendedForRent import \
    UserPropertyDetailsExtendedForRent
from UserPropertyDetailsExtendedForSale import \
    UserPropertyDetailsExtendedForSale
from UserPropertyDetailsExtendedRented import UserPropertyDetailsExtendedRented

from ..base_schema import BaseSchema


class UserPropertiesResponse(BaseSchema):

    properties: (
        UserPropertyDetailsExtendedForSale
        | UserPropertyDetailsExtendedForRent
        | UserPropertyDetailsExtendedRented
        | UserPropertyDetailsExtended
        | UserPropertyBasicDetails
    )
    _metadata: RequestMetadataWithLinks

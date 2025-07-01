import typing

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .user_property_basic_details import UserPropertyBasicDetails


class UserPropertyDetails(BaseSchema):
    value: typing.List[
        typing.TypedDict("", {"used_by": typing.List[BasicUser]})
        | UserPropertyBasicDetails
    ]

import typing

from BasicUser import BasicUser
from UserPropertyBasicDetails import UserPropertyBasicDetails

from ..base_schema import BaseSchema


class UserPropertyDetailsExtendedForSale(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "", {"used_by": typing.List[BasicUser], "status": str, "cost": int}
        )
        | UserPropertyBasicDetails
    ]

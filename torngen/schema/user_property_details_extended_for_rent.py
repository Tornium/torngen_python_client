import typing

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .user_property_basic_details import UserPropertyBasicDetails


class UserPropertyDetailsExtendedForRent(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "",
            {
                "used_by": typing.List[BasicUser],
                "status": str,
                "renter_asked": BasicUser,
                "rental_period": int,
                "cost_per_day": int,
                "cost": int,
            },
        )
        | UserPropertyBasicDetails
    ]

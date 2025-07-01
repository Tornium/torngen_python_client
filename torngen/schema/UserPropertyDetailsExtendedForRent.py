import typing

from BasicUser import BasicUser
from UserPropertyBasicDetails import UserPropertyBasicDetails

from ..base_schema import BaseSchema


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

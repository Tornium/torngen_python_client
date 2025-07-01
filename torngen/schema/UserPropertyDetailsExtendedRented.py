import typing

from BasicUser import BasicUser
from UserPropertyBasicDetails import UserPropertyBasicDetails

from ..base_schema import BaseSchema


class UserPropertyDetailsExtendedRented(BaseSchema):
    value: typing.List[
        typing.TypedDict(
            "",
            {
                "used_by": typing.List[BasicUser],
                "status": str,
                "rental_period_remaining": int,
                "rental_period": int,
                "cost_per_day": int,
                "cost": int,
            },
        )
        | UserPropertyBasicDetails
    ]

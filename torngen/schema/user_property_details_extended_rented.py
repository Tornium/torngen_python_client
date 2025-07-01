import typing

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .user_property_basic_details import UserPropertyBasicDetails


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

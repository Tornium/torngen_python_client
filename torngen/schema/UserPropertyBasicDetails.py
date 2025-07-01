import typing

from BasicProperty import BasicProperty
from BasicUser import BasicUser
from PropertyId import PropertyId
from PropertyModificationEnum import PropertyModificationEnum
from PropertyStaffEnum import PropertyStaffEnum

from ..base_schema import BaseSchema


class UserPropertyBasicDetails(BaseSchema):

    upkeep: typing.TypedDict("", {"staff": int, "property": int})
    staff: typing.List[typing.TypedDict("", {"type": PropertyStaffEnum, "amount": int})]
    property: BasicProperty
    owner: BasicUser
    modifications: typing.List[PropertyModificationEnum]
    market_price: int
    id: PropertyId
    happy: int

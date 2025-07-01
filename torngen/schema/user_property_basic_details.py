import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_property import BasicProperty
from .basic_user import BasicUser
from .property_id import PropertyId
from .property_modification_enum import PropertyModificationEnum
from .property_staff_enum import PropertyStaffEnum


@dataclass
class UserPropertyBasicDetails(BaseSchema):
    """
    JSON object of `UserPropertyBasicDetails`.
    """

    upkeep: typing.TypedDict("", {"staff": int, "property": int})
    staff: typing.List[typing.TypedDict("", {"type": PropertyStaffEnum, "amount": int})]
    property: BasicProperty
    owner: BasicUser
    modifications: typing.List[PropertyModificationEnum]
    market_price: int
    id: PropertyId
    happy: int

    @staticmethod
    def parse(data):
        return UserPropertyBasicDetails(
            upkeep=BaseSchema.parse(
                data.get("upkeep"),
                typing.TypedDict("", {"staff": int, "property": int}),
            ),
            staff=BaseSchema.parse(
                data.get("staff"),
                typing.List[
                    typing.TypedDict("", {"type": PropertyStaffEnum, "amount": int})
                ],
            ),
            property=BaseSchema.parse(data.get("property"), BasicProperty),
            owner=BaseSchema.parse(data.get("owner"), BasicUser),
            modifications=BaseSchema.parse(
                data.get("modifications"), typing.List[PropertyModificationEnum]
            ),
            market_price=BaseSchema.parse(data.get("market_price"), int),
            id=BaseSchema.parse(data.get("id"), PropertyId),
            happy=BaseSchema.parse(data.get("happy"), int),
        )

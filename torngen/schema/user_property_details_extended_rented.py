import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_property import BasicProperty
from .basic_user import BasicUser
from .property_id import PropertyId
from .property_modification_enum import PropertyModificationEnum
from .property_staff_enum import PropertyStaffEnum


@dataclass
class UserPropertyDetailsExtendedRented(BaseSchema):

    used_by: typing.List[BasicUser]
    status: str
    rental_period_remaining: int
    rental_period: int
    cost_per_day: int
    cost: int
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
        return UserPropertyDetailsExtendedRented(
            used_by=BaseSchema.parse(data.get("used_by"), typing.List[BasicUser]),
            status=BaseSchema.parse(data.get("status"), str),
            rental_period_remaining=BaseSchema.parse(
                data.get("rental_period_remaining"), int
            ),
            rental_period=BaseSchema.parse(data.get("rental_period"), int),
            cost_per_day=BaseSchema.parse(data.get("cost_per_day"), int),
            cost=BaseSchema.parse(data.get("cost"), int),
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

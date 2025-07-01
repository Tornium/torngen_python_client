import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_property_details import UserPropertyDetails


@dataclass
class UserPropertyResponse(BaseSchema):
    """
    JSON object of `UserPropertyResponse`.
    """

    property: UserPropertyDetails

    @staticmethod
    def parse(data):
        return UserPropertyResponse(
            property=BaseSchema.parse(data.get("property"), UserPropertyDetails),
        )

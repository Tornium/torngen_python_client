import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_property_details_extended_with_rent import (
    UserPropertyDetailsExtendedWithRent,
)


@dataclass
class PropertyPropertyResponse(BaseSchema):
    """
    JSON object of `PropertyPropertyResponse`.
    """

    property: UserPropertyDetailsExtendedWithRent

    @staticmethod
    def parse(data):
        return PropertyPropertyResponse(
            property=BaseSchema.parse(
                data.get("property"), UserPropertyDetailsExtendedWithRent
            ),
        )

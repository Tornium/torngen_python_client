import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .property_modification_enum import PropertyModificationEnum
from .property_staff_enum import PropertyStaffEnum
from .property_type_id import PropertyTypeId


@dataclass
class TornProperties(BaseSchema):
    """
    JSON object of `TornProperties`.
    """

    properties: typing.List[
        typing.TypedDict(
            "",
            {
                "upkeep": int,
                "staff": typing.List[PropertyStaffEnum],
                "name": str,
                "modifications": typing.List[PropertyModificationEnum],
                "id": PropertyTypeId,
                "happy": int,
                "cost": int,
            },
        )
    ]

    @staticmethod
    def parse(data):
        return TornProperties(
            properties=BaseSchema.parse(
                data.get("properties"),
                typing.List[
                    typing.TypedDict(
                        "",
                        {
                            "upkeep": int,
                            "staff": typing.List[PropertyStaffEnum],
                            "name": str,
                            "modifications": typing.List[PropertyModificationEnum],
                            "id": PropertyTypeId,
                            "happy": int,
                            "cost": int,
                        },
                    )
                ],
            ),
        )

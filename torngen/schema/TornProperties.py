import typing

from PropertyModificationEnum import PropertyModificationEnum
from PropertyStaffEnum import PropertyStaffEnum
from PropertyTypeId import PropertyTypeId

from ..base_schema import BaseSchema


class TornProperties(BaseSchema):

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

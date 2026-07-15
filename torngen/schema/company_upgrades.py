import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_staff_room_size_enum import CompanyStaffRoomSizeEnum


@dataclass
class CompanyUpgrades(BaseSchema):
    """
    JSON object of `CompanyUpgrades`.
    """

    storage_capacity: int
    storage: str
    staff_room: CompanyStaffRoomSizeEnum

    @staticmethod
    def parse(data):
        return CompanyUpgrades(
            storage_capacity=BaseSchema.parse(data.get("storage_capacity"), int),
            storage=BaseSchema.parse(data.get("storage"), str),
            staff_room=BaseSchema.parse(
                data.get("staff_room"), CompanyStaffRoomSizeEnum
            ),
        )

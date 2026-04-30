import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_staff_room_size_enum import CompanyStaffRoomSizeEnum
from .company_storage_size_enum import CompanyStorageSizeEnum


@dataclass
class CompanyUpgrades(BaseSchema):
    """
    JSON object of `CompanyUpgrades`.
    """

    storage_capacity: CompanyStorageSizeEnum
    storage: str
    staff_room: CompanyStaffRoomSizeEnum

    @staticmethod
    def parse(data):
        return CompanyUpgrades(
            storage_capacity=BaseSchema.parse(
                data.get("storage_capacity"), CompanyStorageSizeEnum
            ),
            storage=BaseSchema.parse(data.get("storage"), str),
            staff_room=BaseSchema.parse(
                data.get("staff_room"), CompanyStaffRoomSizeEnum
            ),
        )

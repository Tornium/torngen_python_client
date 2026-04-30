import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_employee_position import CompanyEmployeePosition
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class CompanyEmployee(BaseSchema):
    """
    JSON object of `CompanyEmployee`.
    """

    status: UserStatus
    position: CompanyEmployeePosition
    name: str
    last_action: UserLastAction
    id: UserId
    days_in_company: int

    @staticmethod
    def parse(data):
        return CompanyEmployee(
            status=BaseSchema.parse(data.get("status"), UserStatus),
            position=BaseSchema.parse(data.get("position"), CompanyEmployeePosition),
            name=BaseSchema.parse(data.get("name"), str),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            id=BaseSchema.parse(data.get("id"), UserId),
            days_in_company=BaseSchema.parse(data.get("days_in_company"), int),
        )

import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_employee_effectiveness import CompanyEmployeeEffectiveness
from .company_employee_position import CompanyEmployeePosition
from .company_employee_stats import CompanyEmployeeStats
from .user_id import UserId
from .user_last_action import UserLastAction
from .user_status import UserStatus


@dataclass
class CompanyEmployeeExtended(BaseSchema):

    wage: int
    value: None | int
    stats: CompanyEmployeeStats
    joined_at: int
    effectiveness: CompanyEmployeeEffectiveness
    status: UserStatus
    position: CompanyEmployeePosition
    name: str
    last_action: UserLastAction
    id: UserId
    days_in_company: int

    @staticmethod
    def parse(data):
        return CompanyEmployeeExtended(
            wage=BaseSchema.parse(data.get("wage"), int),
            value=BaseSchema.parse(data.get("value"), None | int),
            stats=BaseSchema.parse(data.get("stats"), CompanyEmployeeStats),
            joined_at=BaseSchema.parse(data.get("joined_at"), int),
            effectiveness=BaseSchema.parse(
                data.get("effectiveness"), CompanyEmployeeEffectiveness
            ),
            status=BaseSchema.parse(data.get("status"), UserStatus),
            position=BaseSchema.parse(data.get("position"), CompanyEmployeePosition),
            name=BaseSchema.parse(data.get("name"), str),
            last_action=BaseSchema.parse(data.get("last_action"), UserLastAction),
            id=BaseSchema.parse(data.get("id"), UserId),
            days_in_company=BaseSchema.parse(data.get("days_in_company"), int),
        )
